############################################################################################################
# Importing Libraries

import streamlit as st
import hmac
import pandas as pd
import random
import os
import time
import base64
import logging
import io
import config
from openai import OpenAI

############################################################################################################
# Password protection

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

############################################################################################################
# Streamlit app layout

# Set the page to wide or centered mode
st.set_page_config(layout="wide")

# Load the terms file into a DataFrame
df = pd.read_csv(config.default_terms_csv)

# Streamlit app layout
st.title(config.app_title)
st.markdown(config.intro_para)
st.caption(config.app_author)
with st.expander("INSTRUCTIONS FOR STUDENTS:"):
    st.markdown(config.instructions)
with st.expander("**INSTRUCTORS**: For a look at the current terms file driving the interaction, click here:"):
    st.markdown("This is the terms.csv file that drives the interaction. You can edit this file to change the terms and context that the chatbot uses. You may add any term or phrase. You may leave the context blank if you prefer or you can add anything relevant that the GPT does not normally know about the term. This may include relevant learning objectives, course examples, notable scientists, assessment dates, syllabus information, etc.")
    st.table(df)
with st.expander("**INSTRUCTORS**: For a look at the prompt driving the chatbot, click here:"):
    st.markdown(config.display_prompt)
st.sidebar.title(config.sidebar_title)
with st.sidebar:
        with st.expander("Click here for instructions."):
            st.write(config.sidebar_instructions)

############################################################################################################
# File Uploader in sidebar

# Load terms from a CSV file
# https://discuss.streamlit.io/t/how-to-upload-a-csv-file/7052/2
def load_terms(file_input):
    try:
        if isinstance(file_input, str):
            data = pd.read_csv(file_input)
        else:
            data = pd.read_csv(io.StringIO(file_input.read().decode('utf-8')))
        return data
    except Exception as e:
        st.error(f"An error occurred while loading the file: {str(e)}")
        logging.exception(f"Error loading file: {e}")

# Function to create a download link for a file
def create_download_link(file_path, file_name):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode("utf-8")
        download_link = f'<a href="data:file/csv;base64,{encoded_content}" download="{file_name}">Download {file_name}</a>'
        return download_link
    except FileNotFoundError:
        error_message = f"The file {file_name} was not found."
        st.error(error_message)
        logging.exception(error_message)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        st.error(error_message)
        logging.exception(error_message)

# Function to extract the first column values
def get_first_column_values(df):
    if not df.empty:
        return df.iloc[:, 0].tolist()
    else:
        return []

# Download link for the template file
template_file_path = config.default_terms_csv

# File Uploader
uploaded_file = st.sidebar.file_uploader(" ", type=["csv"])
if uploaded_file is not None:
    logging.info(f"File uploaded: {uploaded_file.name}")
    st.session_state.uploaded_file = uploaded_file

# Load terms from the file
if 'uploaded_file' in st.session_state and st.session_state.uploaded_file is not None:
    terms = load_terms(st.session_state.uploaded_file)
else:
    terms = load_terms(template_file_path)

# Extract first column values
term_list = get_first_column_values(terms)

st.sidebar.markdown(create_download_link(template_file_path, "terms.csv"), unsafe_allow_html=True)

# line break in the sidebar
st.sidebar.markdown('<hr>', unsafe_allow_html=True)

############################################################################################################
# Term Selection and session state

# Define a basic initial context at the beginning of your script
initial_context = {
    "role": "system",
    "content": config.initial_prompt
}

# Initialize the session state variables for selected term, context, and display messages
if 'selected_term' not in st.session_state:
    st.session_state.selected_term = None
if 'selected_context' not in st.session_state:
    st.session_state.selected_context = None
if 'display_messages' not in st.session_state:
    st.session_state.display_messages = [initial_context]

# Initialize session states for the selected term, counter, and display flag
if 'selected_term' not in st.session_state:
    st.session_state.selected_term = None
if 'display_term' not in st.session_state:
   st.session_state.display_term = False

# Dropdown menu for selecting a term
selected_term = st.selectbox('Select a term/question and brainstorm everything about it. This could include a definition, examples, misconceptions, associations, etc.', term_list)
if selected_term:
    selected_context = terms.loc[terms['TERM'] == selected_term, 'CONTEXT'].values[0]
    st.session_state.selected_term = selected_term
    st.session_state.selected_context = selected_context
    st.session_state.display_term = True

# Ensure the session state variables are set correctly
# if st.session_state.get('selected_term') and st.session_state.get('selected_context'):
    # Update the prompt for the API
    updated_prompt = config.term_prompt(st.session_state.selected_term, st.session_state.selected_context, term_list)
    initial_context = {
        "role": "system", 
        "content": updated_prompt
    }
    # Reset the conversation with the new initial context
    st.session_state.display_messages[0] = [initial_context]

# Display the selected term and its context
if st.session_state.display_term and st.session_state.selected_term:
    st.header(st.session_state.selected_term)
    # Pass the displayed term to the assistant as part of the message
    user_message = f"Define '{st.session_state.selected_term}':"
elif not st.session_state.selected_term:
    st.write("")

############################################################################################################
# ChatGPT
# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize the session state variables if they don't exist
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = config.ai_model

if "display_messages" not in st.session_state:
    st.session_state.display_messages[0] = [initial_context]

# Update initial_context with the latest selected term and context
if st.session_state.get('selected_term') and st.session_state.get('selected_context'):
    updated_prompt = config.term_prompt(st.session_state.selected_term, st.session_state.selected_context, term_list)
    initial_context = {
        "role": "system", 
        "content": updated_prompt
    }
    # Replace the initial context in display_messages with the updated prompt
    st.session_state.display_messages[0] = initial_context

# Get user input
prompt = st.chat_input("Type your message here...")

# Input for new messages
if prompt:
    # Ensure the initial context is in the session state, add the user's message
    if not st.session_state["display_messages"]:
        st.session_state["display_messages"].append(initial_context)
    st.session_state["display_messages"].append({"role": "user", "content": prompt})

# Function to reset all chat-related session state
def reset_chat_history():
    st.session_state["display_messages"] = [initial_context]
    # Reset other chat-related session states if they exist
    if 'selected_term' in st.session_state:
        st.session_state.selected_term = None
    if 'selected_context' in st.session_state:
        st.session_state.selected_context = None
    if 'display_term' in st.session_state:
        st.session_state.display_term = False
    st.rerun()

# Main chat container
with st.container(height=400, border=True):
    # Display chat history in reverse order including new messages
    for message in st.session_state["display_messages"][1:]:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(message["content"])

# Generate assistant's response and add it to the messages
    if prompt:
        with st.chat_message("assistant"):
            try:
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state["display_messages"]
                    ],
                    stream=True,
                    temperature=config.temperature,
                    max_tokens=config.max_tokens,
                    frequency_penalty=config.frequency_penalty,
                    presence_penalty=config.presence_penalty,
                )
                response = st.write_stream(stream)
                # Append the full response to the session state for display
                st.session_state["display_messages"].append(
                    {"role": "assistant", "content": response}
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Add Clear Chat History button between container and warning message
if st.button("Clear Chat History"):
    reset_chat_history()

st.markdown(config.warning_message, unsafe_allow_html=True)

############################################################################################################

# Resources and About Sections in the Sidebar

st.sidebar.title("Resources")

for resource in config.resources:
    with st.sidebar:
        with st.sidebar:
            with st.expander(resource["title"]):
                st.markdown(f"Description: {resource['description']}")
                if "url" in resource:
                    st.markdown(f"[{resource['title']}]({resource['url']})")
                if "file_path" in resource:
                    file_path = resource["file_path"]
                    if os.path.exists(file_path):
                        with open(file_path, "rb") as file:
                            file_bytes = file.read()
                        with st.spinner(f"Loading {resource['title']}..."):
                            st.download_button(
                                label=resource["title"],
                                data=file_bytes,
                                file_name=os.path.basename(file_path),
                                mime="application/octet-stream",
                                help=resource["description"],
                            )
                    else:
                        st.warning(f"File not found: {file_path}")

# Footer
with st.sidebar:
    st.markdown("---")

    st.title("About")

   # Using the config objects in your Streamlit app
    st.markdown(config.app_creation_message, unsafe_allow_html=True)
    st.markdown(config.app_repo_license_message, unsafe_allow_html=True)
