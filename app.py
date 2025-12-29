import streamlit as st
import groq
from typing import Optional, Tuple
import re

# Static Groq API Key
GROQ_API_KEY = "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"

# Page configuration
st.set_page_config(
    page_title="Code Explainer App",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Background color */
    .stApp {
        background-color: #6E9FDE;
    }
    .main .block-container {
        background-color: #6E9FDE;
    }
    [data-testid="stSidebar"] {
        background-color: #5a8bc4;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .code-block {
        background-color: #f0f0f0;
        padding: 0.5rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
    }
    </style>
""", unsafe_allow_html=True)

def detect_language(code: str) -> str:
    """
    Simple language detection based on code patterns.
    Returns detected language or 'Unknown'.
    """
    code_lower = code.lower().strip()
    
    # Python indicators
    if any(keyword in code for keyword in ['import ', 'def ', 'print(', 'if __name__']):
        return 'Python'
    
    # JavaScript indicators
    if any(keyword in code for keyword in ['function ', 'const ', 'let ', 'var ', 'console.log', '=>']):
        return 'JavaScript'
    
    # Java indicators
    if any(keyword in code for keyword in ['public class', 'public static void', 'System.out.println']):
        return 'Java'
    
    # C/C++ indicators
    if any(keyword in code for keyword in ['#include', 'int main(', 'printf(', 'cout <<']):
        return 'C/C++'
    
    # HTML indicators
    if '<html' in code_lower or '<div' in code_lower or '<body' in code_lower:
        return 'HTML'
    
    # CSS indicators
    if '{' in code and ':' in code and ('color:' in code_lower or 'margin:' in code_lower):
        return 'CSS'
    
    return 'Unknown'

def get_explanation(code: str, language: str, api_key: str) -> Optional[str]:
    """
    Calls Groq API to get code explanation.
    Returns the explanation text or None if error occurs.
    """
    try:
        client = groq.Groq(api_key=api_key)
        
        system_prompt = """You are a helpful coding tutor. Explain code in simple, beginner-friendly language.
Always provide your response in this exact format:

✅ What this code does

[Provide a 2-3 sentence overview explaining the purpose and functionality of the code]

🔍 Line-by-line explanation

[For each significant line of code, provide an explanation in this format:]
code_line → explanation

[Continue for all important lines]

💡 Suggestions to improve the code

1. [First suggestion with brief explanation]
2. [Second suggestion with brief explanation]
3. [Third suggestion with brief explanation]

Make sure to:
- Use simple language that beginners can understand
- Explain the "what" and "why" of each line
- Focus on clarity over technical jargon
- Provide actionable improvement suggestions
- Format code lines with proper indentation when showing them"""
        
        user_prompt = f"Explain this {language} code:\n\n{code}"
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content
        
    except groq.APIError as e:
        if "401" in str(e) or "authentication" in str(e).lower():
            st.error("❌ Invalid API key. Please check your Groq API key.")
        elif "429" in str(e) or "rate limit" in str(e).lower():
            st.error("❌ Rate limit exceeded. Please wait a moment and try again.")
        else:
            st.error(f"❌ API Error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        return None

def format_explanation_with_styled_headers(explanation: str) -> str:
    """
    Formats the explanation text by wrapping section headers in styled HTML.
    Makes headers bold and 5 points bigger.
    """
    import re
    
    # Define header patterns and their replacements
    header_replacements = [
        (r'(✅\s*What this code does)', r'<div style="font-weight: bold; font-size: calc(1em + 5pt); margin-top: 1rem; margin-bottom: 0.5rem;">\1</div>'),
        (r'(💡\s*Suggestions to improve the code)', r'<div style="font-weight: bold; font-size: calc(1em + 5pt); margin-top: 1rem; margin-bottom: 0.5rem;">\1</div>'),
        (r'(🔍\s*Line-by-line explanation)', r'<div style="font-weight: bold; font-size: calc(1em + 5pt); margin-top: 1rem; margin-bottom: 0.5rem;">\1</div>'),
    ]
    
    formatted_text = explanation
    
    # Apply each replacement
    for pattern, replacement in header_replacements:
        formatted_text = re.sub(pattern, replacement, formatted_text, flags=re.IGNORECASE)
    
    return formatted_text

def validate_api_key(api_key: str) -> bool:
    """
    Basic validation for API key format.
    Groq API keys typically start with 'gsk_' and are 51 characters long.
    """
    if not api_key:
        return False
    if len(api_key) < 20:  # Basic length check
        return False
    return True

def validate_code(code: str) -> Tuple[bool, Optional[str]]:
    """
    Validates code input.
    Returns (is_valid, error_message).
    """
    if not code or not code.strip():
        return False, "Please enter some code to explain."
    
    if len(code) > 10000:  # Roughly 500 lines at 20 chars per line
        return False, "Code is too long. Please limit to approximately 500 lines."
    
    return True, None

# Main App
def main():
    # Header
    st.markdown('<div class="main-header">💡 Code Explainer App</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #666; margin-bottom: 2rem;">
        Get instant, beginner-friendly explanations of your code with AI-powered insights
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        st.markdown("""
        ### 📝 Instructions
        1. Paste your code in the text area
        2. Optionally select the language
        3. Click "Explain Code"
        """)
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📝 Paste your code here:")
        code_input = st.text_area(
            "",
            height=300,
            placeholder="// Example:\nfunction greet(name) {\n    return `Hello, ${name}!`;\n}\n\ngreet('World');",
            label_visibility="collapsed"
        )
    
    with col2:
        st.subheader("🌐 Language")
        # Auto-detect language
        detected_lang = detect_language(code_input) if code_input else "Auto-detect"
        
        language_options = [
            "Auto-detect",
            "Python",
            "JavaScript",
            "Java",
            "C/C++",
            "HTML",
            "CSS",
            "Other"
        ]
        
        selected_language = st.selectbox(
            "",
            options=language_options,
            index=0 if detected_lang == "Auto-detect" or detected_lang == "Unknown" else language_options.index(detected_lang) if detected_lang in language_options else 0,
            label_visibility="collapsed",
            help="Select programming language or use auto-detection"
        )
        
        if selected_language == "Auto-detect" and code_input:
            if detected_lang != "Unknown":
                st.info(f"🔍 Detected: {detected_lang}")
            else:
                st.warning("⚠️ Could not detect language")
    
    # Explain button
    explain_button = st.button("🚀 Explain Code", type="primary", use_container_width=True)
    
    # Process explanation
    if explain_button:
        # Validate inputs
        is_valid_code, code_error = validate_code(code_input)
        if not is_valid_code:
            st.error(f"❌ {code_error}")
            return
        
        # Determine language
        if selected_language == "Auto-detect":
            language = detect_language(code_input)
            if language == "Unknown":
                language = "programming"
        else:
            language = selected_language
        
        # Show loading spinner
        with st.spinner("🤔 Analyzing your code... This may take 10-15 seconds."):
            explanation = get_explanation(code_input, language, GROQ_API_KEY)
        
        if explanation:
            st.markdown("---")
            st.markdown("## 📊 Explanation Results")
            
            # Format and display the explanation with styled headers
            formatted_explanation = format_explanation_with_styled_headers(explanation)
            st.markdown(formatted_explanation, unsafe_allow_html=True)
            
            # Add copy functionality
            st.markdown("---")
            if st.button("📋 Copy Explanation", use_container_width=True):
                st.code(explanation, language="markdown")
                st.success("✅ Explanation copied! (Select and copy from the code block above)")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #999; font-size: 0.9rem; margin-top: 2rem;">
        Built with ❤️ using Streamlit and Groq AI
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

