# Code Reviewer

This project is an AI-powered code reviewing application built using `Pydantic`, `Langchain`, `Streamlit`, `OpenAI GPT-4o-mini`, and `Google's Gemini 1.5 Flash`. It enables users to submit Python code snippets for review, and the AI will analyze the code for potential bugs, provide a bug report, and suggest optimized code.

## Features

- **AI Code Review**: Analyze Python code for bugs and inefficiencies.
- **Code Optimization**: Get an optimized version of your code.
- **Model Selection**: Choose between the GPT-4o-mini model and (optional) Gemini-1.5-Flash.
- **Streamlit Interface**: User-friendly interface to interact with the AI.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MohammedMahboob786/Code-Reviewer.git
   cd Code-Reviewer
   ```

2. **Install dependencies**:

   Create a Virtual Environment and install dependencies.
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Add API Keys**:
   - Create a `key.txt` file in the project root and paste your OpenAI API key in it.
   - Add your Gemini API key in a file named `key2.txt`.

## Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run code_debugger_langchain.py
   ```

2. **Interacting with the app**:
   - Open the browser window that Streamlit launches.
   - Select a model from the sidebar (GPT-4o-mini or Gemini-1.5-Flash).
   - Input your Python code in the text area and click "Generate."

3. **Outputs**:
   - **Code Reviewer**: The app displays a bug report and suggestions in a structured format.
   - **Bug Report**: The app lists potential issues in the provided code.
   - **Optimized Code**: The app outputs an optimized version of the code based on the review.

## API Keys

- **OpenAI**: To use the GPT-4o-mini model, make sure to place your OpenAI API key in `key.txt`.
- **Gemini**: To use the Gemini 1.5 Flash model, make sure to place your Gemini API key in `key2.txt`.