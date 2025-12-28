# 💡 Code Explainer App

A beginner-friendly web application that helps users understand code by providing AI-powered explanations in simple, easy-to-understand language.

## 🎯 Features

- **Code Input**: Large text area for pasting code snippets with automatic language detection
- **AI-Powered Explanations**: Get instant explanations using Groq's Llama 3.1 8B Instant model
- **Line-by-Line Breakdown**: Detailed explanation of each significant line of code
- **Improvement Suggestions**: Receive actionable suggestions to improve your code
- **Simple Interface**: Clean, intuitive UI requiring no setup

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Groq API key (get one free at [Groq Console](https://console.groq.com/))

### Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to the URL shown in the terminal (usually `http://localhost:8501`)

## 📖 Usage

1. **Enter your Groq API key** in the sidebar
2. **Paste your code** in the main text area
3. **Select the language** (or use auto-detection)
4. **Click "Explain Code"** and wait for the AI-powered explanation

## 🎨 Example Output

The app provides three types of explanations:

- ✅ **What this code does**: A 2-3 sentence overview
- 🔍 **Line-by-line explanation**: Detailed breakdown of each important line
- 💡 **Suggestions to improve**: Actionable tips to enhance your code

## 🔧 Technical Details

### Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Groq API with Llama 3.1 8B Instant
- **Language**: Python 3.8+

### Supported Languages

- Python
- JavaScript
- Java
- C/C++
- HTML
- CSS
- And more (with auto-detection)

### API Configuration

- **Model**: `llama-3.1-8b-instant`
- **Temperature**: 0.7
- **Max Tokens**: 2000
- **API Key**: Entered at runtime (not stored)

## ⚠️ Important Notes

- **API Key Security**: Your API key is never stored or logged. It's only used for the current session.
- **Code Privacy**: Your code is sent to Groq API for processing but is not stored by this application.
- **Rate Limits**: Be aware of Groq API rate limits. If you hit a limit, wait a moment and try again.

## 🐛 Troubleshooting

### "Invalid API Key" Error
- Verify your API key is correct
- Make sure there are no extra spaces
- Get a new key from [Groq Console](https://console.groq.com/) if needed

### "Rate Limit Exceeded" Error
- Wait a few moments before trying again
- Groq provides generous free tier limits

### Code Not Explaining
- Check that your code is not empty
- Ensure code is under ~500 lines
- Try selecting the language manually if auto-detection fails

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/) AI
- Uses [Llama 3.1](https://llama.meta.com/) model

---

**Happy Coding! 💻✨**

