# GitSense 🤖✨

### AI-powered Git enhancements for a smarter workflow

GitSense supercharges your Git experience by automating repetitive tasks with AI.  
Generate commit messages, streamline branch naming, and get intelligent suggestions right from your terminal.

## 🔥 Features

- **Smart Commit Messages**: Automatically generate meaningful commit messages from `git diff`.
- **Lightning Fast**: Runs locally or via GeminiAPI.
- **More Featurs**: Coming soon

# 🚀 Quick Start Guide

## 🔑 1. Configuration

### API Key Setup

1. **Get your Google AI Studio API key**:

   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Click on **"Get API key"** (top-right corner)
   - Create and copy your API key

2. **Configure your environment**:
   - Open the `.env_example` file in gitsense directory
   - Replace `<KEY-HERE>` with your copied API key
   - Rename the file to `.env`

### ⚙️ Model Selection and other settings (Optional)

- View available models: [Gemini API Models](https://ai.google.dev/gemini-api/docs/models)
- To change the default model:
  1. Edit `config.yaml` file in gitsense directory
  2. Update the model name
  3. Save the file
  4. Note: you can change other settings in this file

## 📦 2. Installation

After cloning the repository:

```sh
# Install the package
pip install .

# If you encounter issues, try:
pip3 install .
```

## 🖥️ 3. Usage

Generate commits with:

```sh
gitsense commit
```

> **Note**: You may need to add your Python environment's bin directory to your PATH if the command isn't recognized.
