# AI Chatbot

## Overview
This is an AI-powered chatbot built using **Streamlit, Langchain, and Groq**. The chatbot maintains conversation history and provides responses based on user prompts.

## Features
- **Conversational AI:** Uses Groq's Llama model to generate responses.
- **Memory Retention:** Stores chat history using `ConversationBufferMemory`.
- **Streamlit UI:** Simple and interactive web interface.
- **Chat Persistence:** Maintains past user interactions within a session.
- **Reset Chat:** Clear chat history with a button click.

## Technologies Used
- **Streamlit**: For creating the web application.
- **Langchain**: For conversation management.
- **Groq API**: To access the Llama model for AI responses.
- **Python**: Primary programming language.

## Installation & Setup

### Prerequisites
Ensure you have Python installed (>=3.8). You also need `pip` for package management.

### Steps to Run
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo/chatbot.git
   cd chatbot
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up API Key**
   - Create a `.env` file in the project directory.
   - Add your Groq API key:
     ```sh
     GROQ_API_KEY=your_api_key_here
     ```

5. **Run the Chatbot**
   ```sh
   streamlit run app.py
   ```

## Usage
- Open the chatbot interface in your browser.
- Type a message in the chat input field.
- The AI will generate a response and maintain conversation history.
- Use the sidebar to **clear chat history** when needed.

## Customization
- Change the **model name** in `app.py`:
  ```python
  model_name = 'llama-3.3-70b-versatile'
  ```
- Adjust the **temperature** (controls randomness of responses):
  ```python
  temperature=0.7
  ```

## License
This project is open-source and available under the [Apache License 2.0](LICENSE).



Feel free to contribute and improve the chatbot!

