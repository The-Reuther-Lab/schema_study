# Schema Study: An AI-Enhanced Study App for Biology Students

Welcome to the DIY AI-Enhanced Study App repository. This application is designed to help biology students learn and assess their knowledge of core course concepts through interactive study sessions. Educators can customize the app by uploading their own terms and schemas, and students can engage with an AI-powered chatbot to receive instant feedback and guidance.

## Features

- **Password Protection:** Secure access to the app.
- **Customizable Terms:** Upload your own CSV file with terms and schemas.
- **Random Term Selection:** Randomly pick terms for study sessions.
- **AI-Enhanced Feedback:** Utilize OpenAI's GPT-4o model to provide definitions, explanations, and formative feedback.
- **Interactive Chat:** Engage in a conversation with the AI chatbot to deepen understanding.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- OpenAI API Key

### Installation

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

### Usage

1. **Run the App:**

```bash
streamlit run app.py
```

2. **Access the App:**

Open your web browser and go to `http://localhost:8501`. You will be prompted to enter the password.

3. **Upload Terms:**

Upload your CSV file with terms and schemas through the sidebar file uploader. The file should have two columns: `TERM` and `SCHEMA`.

4. **Start Studying:**

Click the button to pick a random term, and start your interactive study session with the AI chatbot.

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

Developed by Keefe Reuther, Assistant Teaching Professor in the UC San Diego School of Biological Sciences. Special thanks to the members of the Reuther Lab for their support and contributions.