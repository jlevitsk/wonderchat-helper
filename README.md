# wonderchat-helper
A CLI for using the Wonderchat.ai API to update ChatBots

WonderChat.ai Tool
==================

The WonderChat.ai Tool is a Python script that allows you to interact with the WonderChat.ai ChatBot using the WonderChat.ai API. This tool provides functionalities to chat with the ChatBot, add URLs, remove URLs, reindex URLs, and edit the configuration.

Prerequisites
-------------

- Python 3.x
- requests module

Getting Started
---------------

1. Sign up for a free WonderChat.ai account at [https://www.wonderchat.ai](https://www.wonderchat.ai).
2. Clone or download the WonderChat.ai Tool script from the GitHub repository: [https://github.com/your-repo/wonderchat-tool](https://github.com/your-repo/wonderchat-tool).
3. Install the required Python module by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

Usage
-----

Run the script using the following command:

```shell
python wonderutil.py
```

Upon running the script for the first time, it will create a `config.ini` file in the same directory. This file stores the configuration information, including the API token, chatbot ID, and debug mode.

You will be prompted to enter your API token and chatbot ID to configure the tool. Follow the on-screen instructions to set these values.

The tool provides the following options:

- **Chat with Bot (Option 1):** Start a conversation with the ChatBot and receive responses. You can ask follow-up questions and start a new conversation.
- **Add URLs (Option 2):** Add URLs to the ChatBot. Enter the URLs one by one and confirm the addition.
- **Remove URLs (Option 3):** Remove URLs from the ChatBot. Enter the URLs one by one and confirm the removal.
- **Reindex URLs (Option 4):** Reindex URLs in the ChatBot. Enter the URLs one by one and confirm the reindexing.
- **Edit Configuration (Option 5):** Edit the configuration, including the API token, chatbot ID, and debug mode.
- **Quit (Option 6):** Exit the tool.

Configuration
-------------

The configuration is stored in the `config.ini` file. When running the tool for the first time, the script will create this file if it doesn't exist. The file will initially contain placeholder values that you need to update with your actual API token, chatbot ID, and debug mode.

The `config.ini` file has the following JSON format:

```json
{
  "api_token": "REPLACE_WITH_API_KEY",
  "chatbot_id": "REPLACE_WITH_BOT_ID",
  "debug": false
}
```

- `api_token`: Your WonderChat.ai API token.
- `chatbot_id`: The ID of the chatbot you want to interact with.
- `debug`: Set to `true` to enable debug mode, which displays additional information about API calls.

Make sure to replace `REPLACE_WITH_API_KEY` and `REPLACE_WITH_BOT_ID` with your actual API token and chatbot ID.

License
-------

This project is licensed under the [MIT License](LICENSE).

Please update the README with the correct information specific to your project.