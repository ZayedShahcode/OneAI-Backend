# Flask LangChain Chatbot

A web-based AI chatbot application built with Flask and the LangChain framework. This application provides a conversational interface where users can interact with an AI assistant through a clean and responsive web interface.

## Features

- Interactive chat interface
- Support for multiple language models
- Customizable chatbot behavior
- API endpoints for integration with other applications
- Session management for multiple users
- Markdown rendering in responses

## Demo

![Chatbot Demo](/api/placeholder/800/400)

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- API key for your chosen language model (OpenAI, Anthropic, etc.)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-langchain-chatbot.git
   cd flask-langchain-chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Configuration

The application can be configured through the `.env` file:

```
# API Keys
LLM_API_KEY=your_api_key_here
LLM_PROVIDER=openai  # Options: openai, anthropic, etc.

```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```
   Or for development mode:
   ```bash
   flask run --debug
   ```

2. Start chatting with the AI assistant through the web interface



## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
