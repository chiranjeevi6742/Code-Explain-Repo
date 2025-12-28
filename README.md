# 💡 Code Explainer App

A beginner-friendly web application that helps users understand code by providing AI-powered explanations in simple, easy-to-understand language.

## 📱 What Your App Does

The Code Explainer App is a web-based tool designed to help beginners and developers understand code quickly and easily. Here's what it does:

- **Explains Code in Simple Language**: Paste any code snippet and get a clear, beginner-friendly explanation of what it does
- **Line-by-Line Breakdown**: Provides detailed explanations for each significant line of code, making it easy to understand how the code works step-by-step
- **Improvement Suggestions**: Offers actionable suggestions to improve your code, including best practices, performance tips, and style recommendations
- **Multi-Language Support**: Automatically detects or manually select from various programming languages including Python, JavaScript, Java, C/C++, HTML, CSS, and more
- **Instant Results**: Get explanations within 10-15 seconds using AI-powered analysis

Perfect for students learning programming, developers reviewing unfamiliar code, or anyone who wants to quickly understand what a piece of code does.

## 🤖 Which AI Was Used

This app uses **Groq API** with the **Llama 3.1 8B Instant** model:

- **AI Provider**: [Groq](https://groq.com/) - High-performance AI inference platform
- **Model**: `llama-3.1-8b-instant` - Meta's Llama 3.1 model optimized for fast inference
- **Why Groq?**: Groq provides extremely fast AI inference, making it perfect for real-time code explanations
- **API Configuration**:
  - Temperature: 0.7 (balanced creativity and consistency)
  - Max Tokens: 2000 (sufficient for detailed explanations)
  - Response Time: Typically 10-15 seconds

The AI is specifically prompted to provide beginner-friendly explanations, focusing on clarity and educational value rather than technical jargon.

## 🚀 How to Run It

### Step 1: Prerequisites
- **Python 3.8 or higher** installed on your system
- A **Groq API key** (get one free at [Groq Console](https://console.groq.com/))

### Step 2: Clone the Repository
```bash
git clone https://github.com/chiranjeevi6742/Code-Explain-Repo.git
cd Code-Explain-Repo
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- `streamlit` - Web framework for the app
- `groq` - Groq API client library

### Step 4: Run the Application
```bash
streamlit run app.py
```

### Step 5: Use the App
1. The app will open in your browser (usually at `http://localhost:8501`)
2. Enter your **Groq API key** in the sidebar
3. **Paste your code** in the main text area
4. Optionally **select the programming language** (or use auto-detection)
5. Click **"Explain Code"** button
6. Wait 10-15 seconds for the AI-powered explanation

That's it! You'll get a detailed explanation with:
- ✅ What the code does (overview)
- 🔍 Line-by-line breakdown
- 💡 Suggestions for improvement

## 🎯 Features

- **Code Input**: Large text area for pasting code snippets with automatic language detection
- **AI-Powered Explanations**: Get instant explanations using Groq's Llama 3.1 8B Instant model
- **Line-by-Line Breakdown**: Detailed explanation of each significant line of code
- **Improvement Suggestions**: Receive actionable suggestions to improve your code
- **Simple Interface**: Clean, intuitive UI requiring no setup

## 📖 Usage Guide

Once the app is running:

1. **Enter your Groq API key** in the sidebar (required for AI explanations)
2. **Paste your code** in the main text area
3. **Select the language** from the dropdown (or use auto-detection)
4. **Click "Explain Code"** button
5. **Wait 10-15 seconds** for the AI to analyze and explain your code
6. **Review the results**:
   - Overall explanation of what the code does
   - Line-by-line breakdown
   - Suggestions for improvement

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

