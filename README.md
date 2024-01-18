# XLAB Bot

# Chatbot using GPT-4-All Pretrained Models

## Overview

This repository contains a simple chatbot created using pretrained models available on GPT-4-All. The chatbot leverages the power of GPT-4 to generate human-like responses and engage in natural language conversations.

## Requirements

To run the chatbot, you need the following dependencies:

* Python (version 3.x)
* [GPT-4-All]() pretrained models (specifically, the model weights and configuration files)
* API Key [Optional : needed for realtime google search]

## Getting Started

1. clone this repo:

   ```

    git clone https://github.com/nizamuddinsyed/XLAB-Bot

    cd XLAB-Bot

   ```
2. Download the GPT-4-All pretrained model weights and configuration files. Ensure they are placed in the appropriate directory (e.g., models/).
3. Install the required Python packages:

   ```

    pip install -r requirements.txt

   ```
4. Run the chatbot

   ```

    chainlit run app.py

   ```

## Usage

Once the chatbot is running, a new window will open in a browser localhost, you can interact with it by typing messages. The chatbot will respond with generated text based on the input it receives.

```
    User: Hello
    Chatbot: Hi there! How can I help you today?

    User: What's the weather like?
    Chatbot: I'm sorry, I don't have the capability to check the weather. However, I can assist you with a variety of topics. Just let me know what you're interested in!
  
```

## Customization

Feel free to customize and extend the chatbot based on your specific use case. You can modify the conversation handling logic, integrate external APIs, or add additional features to enhance the chatbot's capabilities.

## Disclaimer

This chatbot is a basic demonstration and may not be suitable for production use without further enhancements and testing. Use it responsibly and be aware of the limitations of pretrained models

## License

This project is licensed under the MIT License
