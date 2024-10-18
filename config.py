# config.py

# THIS IS THE FILE YOU SHOULD EDIT TO CUSTOMIZE THE APP. DO NOT EDIT app.py UNLESS YOU KNOW WHAT YOU ARE DOING.

############################################################################################################

# Below is the configuration for the chatbot

# The model_name refers to the name of the model you want to use. You can choose from the following models: 
ai_model = "gpt-4o"

# Temperature refers to the randomness/creativity of the responses. A higher temperature will result in more random/creative responses. It varies between 0 and 1.
temperature = 0.1

# Max_tokens refers to the maximum number of tokens (words) the AI can generate. The higher the number, the longer the response. It varies between 1 and 2048.
max_tokens = 1000

# Frequency penalty parameter for the response. Higher penalty will result in more diverse responses. It varies between 0 and 1.
frequency_penalty = 0.5

# Presence penalty parameter for the response. Higher penalty will result in less repetitive responses. It varies between 0 and 1.
presence_penalty = 0.4

# Below is all the text you can customize for the app. Don't remove the quotations around the text. Don't change the variable names.

############################################################################################################

# Below is the name for your default csv terms file. You can change this to any csv file you want to use as your default terms file. It must be in the same folder as the main app.py file.

default_terms_csv = "terms_template.csv"

############################################################################################################

# Below is all the text you can customize for the app. Don't remove the quotations around the text. Don't change the variable names.

# The title of the app
app_title = "Schema Study"

# The subtitle of the app
app_author = "by Keefe Reuther and Liam O Mueller, Assistant Teaching Professors in the UC San Diego School of Biological Sciences"

# This is an intro paragraph you can add under the title. it is not currently being used in the app.
intro_para = "An AI-enhanced study app for biology students."

# The user's instructions for the app
instructions = '''
The goal of this app is to help you learn and and assess your knowledge of core course concepts and examples. 
1. Choose a course term/phrase from the drop down menu.
2. *Pause and think for 30 seconds.* What is everything you associate with this term/phrase? What is a simple definition or example?
3. Write as little or as much as you'd like about it. Try to include anything you might need to know for an exam. 
4. Please follow-up with questions. If you don't know something, just ask. It is perfectly ok to write: "I have no idea what this term means." **Have a conversation!**
---
**WANT TO LEVEL UP?**
- Ask the chatbot: 'Choose 2 additional terms from the course and prompt me to connect them in a hypothetical scenario.'
- Ask the chatbot: 'Please give me an example mathematical problem that uses this term.'
- Ask the chatbot: 'Please tell me two truths and a lie about this term. I need to choose the lie and explain my reasoning'
- **Get creative! Play around and see what happens!**
'''

# The title of the sidebar
sidebar_title = "Have your own terms to study?"

# The instructions for the template
sidebar_instructions = "Do you have your own terms to study? If so, download the terms_template.csv file. You can delete everything below the first row and add in your own terms in the first column. You can open and edit it in Excel, Google Sheets, or any text editor. Make sure that you don't change the file extension from csv. Once done, upload it below. The app will use your terms for the study session."

app_creation_message = "The template for this app was created by Keefe Reuther, Liam O Mueller, and the members of the Reuther Lab - [https://reutherlab.biosci.ucsd.edu/](https://reutherlab.netlify.app/)"

app_repo_license_message = "It can be found at [https://github.com/The-Reuther-Lab/schema_study](https://github.com/The-Reuther-Lab/schema_study) and is distributed under the GNU GPL-3 License."

warning_message = "**ChatGPT can make errors and does not replace verified and reputable online and classroom resources.**"

############################################################################################################

### PROMPTS

# Below is the initial prompt that the AI will use to start the conversation with the user. The user will not see this prompt.
initial_prompt = (
    "You are a knowledgeable assistant in university-level biology helping a student in a college course. "
    "Your goal is to provide concise, accurate, and supportive responses to assist the student's understanding of biology concepts. "
    "Use the Socratic Method: Encourage critical thinking by asking guiding questions based on the student's input. "
    "Positive Reinforcement: Gently correct misconceptions or errors, acknowledging correct aspects and building upon the student's existing knowledge. "
    "Adjust Explanations: Tailor your explanations to the student's level, defining technical terms when they first appear. "
    "Universal Examples: Use examples and analogies that are widely understood across different cultures. "
    "Clear and Flexible Responses: Keep responses clear and structured, allowing flexibility in length to address the student's needs adequately. "
    "Graceful Redirection: If the student goes off-topic, gently steer the conversation back to relevant biology topics. "
    "Natural Engagement: End responses with an open invitation for further questions to keep the dialogue engaging. "
    "Focus on Understanding: Avoid extraneous language or general statements about performance; concentrate on fostering comprehension and connecting biology concepts."
)

# Below is the follow-up prompt that the AI will use once the user has typed a message. The user will not see this prompt.
# DO NOT REMOVE/EDIT anything outside of the triple quotations or anything inside the curly braces
def term_prompt(selected_term, selected_schema, term_list):
    return f"""You are a knowledgeable assistant in university-level biology course helping a student. Your goal is to provide concise, accurate, and supportive responses to assist the student's understanding of the term '{selected_term}'.

- Use the following information to guide your response: '{selected_schema}'. Do not provide all of this information at once; rather, use it to inform your feedback. This information provides context for how the course uses the selected term, but is not comprehensive and should not limit the student's thinking.
- Provide formative feedback in a clear, succinct way, gently correcting any factual errors and acknowledging correct aspects of the student's input.
- Employ the Socratic method by asking guiding questions that encourage critical thinking and help the student expand their understanding.
- Help the student identify any misconceptions, especially if they mention one in their message.
- Assist them in finding relevant connections between '{selected_term}' and other terms from the course, which include: '{term_list}'.
- Make your responses clear and structured.
- Your goal is to stimulate conversation with the student and help them understand the term.
- Use universal examples and analogies that are accurate and culturally inclusive.
- Avoid extraneous language and focus on fostering comprehension.
- If the student asks a question that appears to be a direct exam question, guide them to think through the answer themselves rather than providing the answer.
- If the student goes off-topic of biology, course content, or likely mentorship topics, gently steer the conversation back to preferred topics.
- Regardless of chat history, You may only answer considering their current message in relation to the term '{selected_term}'. The only exception is if they explicitly ask about another term or concept.
- End your responses with an open invitation for further questions to keep the dialogue engaging."""


############################################################################################################

### RESOURCES

# Resources: In this section, you can add links for the student to access and potentially learn more about the topic or verify information.
# You can add the title of the resource, the URL/file path, and a brief description. To delete or add more resources, follow the same format.
resources = [
    {
        "title": "Course Syllabus",
        "file_path": "syllabus-template.docx",
        "description": "Download the course syllabus. **Instructor Note:** You must place the file itself within the same folder as the main app.py file in your GitHub repository."
    },
    # In this next line you can add a URLs to the resources section. Just edit the current URL and description. If you need more lines, just copy and paste to add an additional resource. Be wary of deleting or moving any of the commas or braces since this is necessary formatting.
    {
        "title": "OpenAI Prompt engineering guide",
        "url": "https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results",
        "description": "A guide to help you craft effective prompts for the OpenAI chatbot. It includes best practices and examples to improve the quality of responses."
    },
    {
        "title": "UC Berkeley Library Guide to Detecting Fake News",
        "url": "https://guides.lib.berkeley.edu/fake-news",
        "description": "This UC Berkeley Library guide offers comprehensive strategies and resources for identifying fake news, understanding its impact, and evaluating the credibility of various news sources, including lists of known fake news sites and tips for detecting misinformation."
    },
        {
        "title": "Is it cheating to use ChatGPT?",
        "url": "https://guides.lib.berkeley.edu/fake-news",
        "description": "The UC San Diego Academic Integrity Office provides guidance on the appropriate use of generative AI tools in educational settings, emphasizing the importance of adhering to instructor guidelines and the potential consequences of misuse, including integrity violations and academic penalties."
    },
    {
        "title": "OpenStax - Biology",
        "url": "https://openstax.org/details/books/biology",
        "description": "Provides free, peer-reviewed, openly licensed textbooks for introductory college and AP-level biology courses."
    },
    {
        "title": "Scitable by Nature Education",
        "url": "https://www.nature.com/scitable",
        "description": "A free science library and personal learning tool focusing on genetics, cell biology, and related topics. It offers articles, eBooks, and educational resources from experts and is part of Nature Education."
    }
]

