# AI Assistant

A command-line AI assistant built from scratch in Python — combines user profile management, persistent chat history, and real AI-powered conversations using Google's Gemini API.

## Features

- User profile setup (name, age, city, learning goal) with input validation
- Real AI-powered chat — powered by Gemini, not scripted responses
- Persistent chat history (saved across sessions as JSON)
- Chat statistics (total messages, word count, longest/shortest message)
- Robust error handling (invalid input, corrupted data files, API failures with automatic retry)
- Built using Object-Oriented Programming (`ChatSession` class manages chat state and behavior)

## Project Structure

```
ai_assistant/
├── src/
│   ├── main.py              # App entry point, menu, ChatSession class
│   ├── ai_client.py         # Gemini API integration with retry logic
│   ├── error_handling.py    # Input validation helpers
│   ├── file_handler.py      # Save/load chat history & user profile (JSON)
│   ├── data/
│   │   ├── chat_history.json
│   │   └── user_profile.json
│   └── test_api_files/      # API learning/practice scripts
├── .env                     # API keys (not committed - see Setup)
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

1. Clone the repo and navigate into it:
   ```
   git clone <your-repo-url>
   cd ai_assistant
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/Scripts/activate   # Windows (Git Bash)
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your Gemini API key:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```
   Get a free key at [Google AI Studio](https://aistudio.google.com).

## How to Run

```
cd src
python main.py
```

## Built With

- Python 3
- Google Gemini API (`google-genai`)
- `python-dotenv` for environment variable management

## What I Learned

Built as part of a 15-day Python fundamentals sprint — covers OOP (classes, inheritance), file I/O, JSON handling, REST API integration, error handling/retry logic, and Git workflow (branching, pull requests).

## Future Improvements

- Conversation memory/context across multiple messages in a single chat (currently each message is sent independently)
- Streaming responses instead of waiting for the full reply
- Support for multiple AI providers (Claude, OpenAI) with a provider switch
- Basic RAG (retrieval-augmented generation) to let the assistant answer questions from custom documents

## Author

Adithya Jannu