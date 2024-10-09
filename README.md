# Schema Study: An AI-Enhanced Study App for Biology Students

Schema Study is a DIY AI-Enhanced Study App designed to assist biology students in mastering core course concepts through interactive study sessions. This application leverages AI technology to provide instant feedback and guidance, making it a valuable tool for both students and educators.

## Pedagogical Value

Schema Study enhances the learning experience by:

- **Promoting Active Learning:** Students engage with course material interactively, which helps reinforce their understanding.
- **Providing Instant Feedback:** The AI-powered chatbot offers immediate responses, allowing students to correct misconceptions in real-time.
- **Encouraging Critical Thinking:** By using the Socratic method, the app guides students to explore concepts deeply and make connections between different terms.
- **Customizable Content:** Educators can tailor the app to their curriculum by uploading specific terms and schemas, ensuring relevance to their course.

## Features

- **Password Protection:** Ensures secure access to the app.
- **Customizable Terms:** Educators can upload a CSV file with their own terms and schemas.
- **AI-Enhanced Feedback:** Utilizes OpenAI's GPT-4o model to provide detailed explanations and formative feedback.
- **Interactive Chat:** Engages students in a dialogue with the AI chatbot to deepen their understanding.

## How the App Works

### For Students

1. **Access the App:** Open your web browser and navigate to `http://localhost:8501`. Enter the password when prompted.
2. **Upload Terms:** Use the sidebar file uploader to upload a CSV file containing terms and schemas. The file should have two columns: `TERM` and `SCHEMA`.
3. **Start Studying:** Click the button to select a random term and begin your interactive study session with the AI chatbot.
4. **Engage with the AI:** Use the chat interface to ask questions and receive feedback on your understanding of the term.

### For Instructors

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/keefereuther/schema_study.git
   cd schema_study
   ```

2. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your Configuration:**

   Update the `config.py` file with your desired settings.

4. **Create a '.streamlit/secrets.toml' file and directory.**

   Add your OpenAI API key and the app password:

   ```toml
   [general]
   OPENAI_API_KEY = "your-openai-api-key"
   password = "your-app-password"
   ```

5. **Run the App:**

   ```bash
   streamlit run app.py
   ```

## Configuration

The `config.py` file contains customizable settings for the app. Key settings include:

- `app_title`: The title of the app.
- `app_author`: Author information.
- `instructions`: Instructions for using the app.
- `sidebar_title`: Title for the sidebar section.
- `default_terms_csv`: Default CSV file for terms.
- AI model settings like `ai_model`, `temperature`, `max_tokens`, `frequency_penalty`, and `presence_penalty`.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the GNU GPL-3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Developed by Keefe Reuther and Liam O Mueller, Assistant Teaching Professors in the UC San Diego School of Biological Sciences. Special thanks to the members of the Reuther Lab for their support and contributions.