# 🤖 Streamlit-Ollama Chatbot

A full-featured chatbot application built with **Streamlit** and **Ollama** for local LLM inference. Chat with AI models running entirely on your machine!

## ✨ Features

- 💬 **Interactive Chat Interface** - Clean, modern UI with message history
- 🔄 **Real-time Streaming** - See responses as they're generated
- 🧠 **Conversation Memory** - Maintains context throughout the chat session
- 🎛️ **Customizable Settings** - Adjust model, temperature, and max tokens
- 🔒 **100% Local & Private** - All processing happens on your machine
- 🎨 **Beautiful UI** - Professional design with dark mode support

## 📋 Prerequisites

Before running this application, make sure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running
   - Download from: https://ollama.ai
   - Install at least one model (e.g., `ollama pull llama3.2`)

## 🚀 Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd Streamlit-langchain
   ```

2. **Activate your virtual environment**
   ```bash
   .\llm-venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Make sure Ollama is running**
   ```bash
   ollama serve
   ```

2. **Pull a model if you haven't already**
   ```bash
   ollama pull llama3.2
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser** to the URL shown (usually http://localhost:8501)

## 🎨 Available Models

The chatbot supports various Ollama models:
- `llama3.2` - Latest Llama model (recommended)
- `llama3.1` - Previous Llama version
- `mistral` - Mistral AI model
- `codellama` - Specialized for coding tasks
- `phi3` - Microsoft's compact model

To use a model, first pull it with Ollama:
```bash
ollama pull <model-name>
```

## ⚙️ Configuration Options

### Temperature (0.0 - 1.0)
- **Lower values (0.0-0.3)**: More focused and deterministic responses
- **Medium values (0.4-0.7)**: Balanced creativity and coherence
- **Higher values (0.8-1.0)**: More creative and random responses

### Max Tokens
- Controls the maximum length of responses
- Range: 100 - 4096 tokens

## 🛠️ Troubleshooting

### "Connection Error" or "Model not found"
- Ensure Ollama is running: `ollama serve`
- Verify the model is installed: `ollama list`
- Pull the model if needed: `ollama pull llama3.2`

### Slow responses
- Try a smaller model (e.g., `phi3`)
- Reduce max tokens
- Check your system resources

### Port already in use
```bash
streamlit run main.py --server.port 8502
```

## 📁 Project Structure

```
Streamlit-langchain/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (optional)
├── llm-venv/           # Virtual environment
└── README.md           # This file
```

## 🔧 Technical Details

- **Frontend**: Streamlit
- **LLM Integration**: LangChain with Ollama
- **Message Handling**: LangChain Core Messages
- **Session Management**: Streamlit Session State

## 📝 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork, modify, and improve this chatbot!

## 📞 Support

If you encounter issues:
1. Check that Ollama is running
2. Verify your model is installed
3. Ensure all dependencies are installed
4. Check the terminal for error messages

---

**Made with ❤️ using Streamlit & Ollama**
