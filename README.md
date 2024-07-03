# ChatBode

Welcome to the ChatBode application repository! This project leverages Streamlit and LangChain to create an interactive, user-friendly chatbot interface. The bot is designed to assist users by answering their questions and maintaining a coherent conversation history.

![ChatBode Logo](https://huggingface.co/recogna-nlp/bode-7b-alpaca-pt-br/resolve/main/Logo_Bode_LLM_Circle.png)

## Features

- **Interactive Chat Interface**: Built with Streamlit, providing a smooth and responsive user experience.
- **Conversation History**: Maintains chat history for context-aware responses.
- **Environment Variable Management**: Securely manages API keys and other sensitive information using a `.env` file.
- **Dynamic Responses**: Utilizes LangChain and ChatCohere for generating and streaming real-time responses.

## Installation

To get started with the ChatBot application, follow these steps:

1. **Clone the repository**:

    ```sh
    git clone https://github.com/joaovitormarianocorreia/chatbode.git
    cd chatbode
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**:

    Create a `.env` file in the root directory of the project and add your API keys:

    ```env
    COHERE_API_KEY=your_actual_api_key_here
    ```

5. **Run the application**:

    ```sh
    streamlit run src/app.py
    ```

## Usage

- **Chat with the Bot**: Enter your queries in the chat input, and the bot will respond in real-time.
- **Session Management**: The bot maintains the chat history within the session to provide contextually relevant responses.

## Contributing

We welcome contributions to improve this project! Please fork the repository and submit pull requests with your enhancements or bug fixes.

## Acknowledgments

- **Streamlit**: For the powerful framework that simplifies the creation of web apps.
- **LangChain**: For the seamless integration with language models.

Feel free to open issues or contact us for further assistance. Enjoy chatting with ChatBode!
