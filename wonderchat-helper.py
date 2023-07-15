import requests
import json
import sys
import time

        
def load_config():
    """Load the configuration from .env file."""
    try:
        with open('.env', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        config = {
            'api_token': 'REPLACE_WITH_API_KEY',
            'chatbot_id': 'REPLACE_WITH_BOT_ID',
            'debug': False
        }
        with open('.env', 'w') as config_file:
            json.dump(config, config_file)

    api_token = config['api_token']
    chatbot_id = config['chatbot_id']
    debug = config.get('debug', False)
    return api_token, chatbot_id, debug



def save_config(api_token, chatbot_id, debug):
    """Save the configuration to .env file."""
    config = {
        'api_token': api_token,
        'chatbot_id': chatbot_id,
        'debug': debug
    }
    with open('.env', 'w') as config_file:
        json.dump(config, config_file)


def chat_with_bot(api_token, chatbot_id, debug):
    """Chat with the chatbot."""
    if not api_token or not chatbot_id:
        print("API Token and Chatbot ID must be valid.")
        return

    endpoint = 'https://app.wonderchat.io/api/v1/chat'
    headers = {'Content-Type': 'application/json'}
    chatlog_id = None

    while True:
        if chatlog_id:
            question = input("Enter your follow-up question ('q' to quit, 'n' to start a new conversation): ")
            if question.lower() == 'q':
                break
            elif question.lower() == 'n':
                chatlog_id = None
                continue
            data = {
                "chatbotId": chatbot_id,
                "question": question,
                "chatlogId": chatlog_id
            }
        else:
            question = input("Enter your question ('q' to quit, 'n' to start a new conversation): ")
            if question.lower() == 'q':
                break
            elif question.lower() == 'n':
                chatlog_id = None
                continue
            data = {
                "chatbotId": chatbot_id,
                "question": question
            }

        if debug:
            print("\nAPI Query:")
            print("Endpoint:", endpoint)
            print("Headers:", headers)
            print("Data:", json.dumps(data, indent=4))

            input("\nPress any key to continue...")

        retry_count = 0
        while retry_count < 10:
            try:
                response = requests.post(endpoint, headers=headers, json=data, timeout=30)
                if response.status_code == 200:
                    api_response = response.json()
                    print("Response:", api_response['response'])
                    chatlog_id = api_response['chatlogId']
                    break
                else:
                    print("\nStatus code:", response.status_code)
                    print("Error in API response: ", response.text)
                    print("Attempt", retry_count+1, "of 10. Retrying...")
                    retry_count += 1
                    time.sleep(1)
            except Exception as e:
                print(f"An error occurred: {e}. Retrying...")
                retry_count += 1
                time.sleep(1)

        if retry_count == 10:
            print("Failed to get a response after 10 retries. Returning to question prompt.")

from urllib.parse import urlparse

def validate_url(url):
    if url and url.startswith(('http://', 'https://')) and urlparse(url).netloc:
        return True
    else:
        print("Invalid URL. Please enter a valid URL that starts with 'http://' or 'https://'.")
        return False

def add_urls(api_token, chatbot_id, debug):
    """Add URLs to the chatbot."""
    print("\nEnter URLs to add (one URL per line, end with Ctrl+D):")
    urls = []
    while True:
        try:
            url = input()
            if validate_url(url):
                urls.append(url)
        except EOFError:
            break

    print("\nURLs to be added:")
    for url in urls:
        print(url)

    confirm = input("\nDo you confirm adding these URLs? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Operation cancelled.")
        return

    endpoint = 'https://app.wonderchat.io/api/v1/add-pages'
    headers = {'Content-Type': 'application/json'}
    data = {
        "apiKey": api_token,
        "chatbotId": chatbot_id,
        "urls": urls
    }
    if debug:
        print("\nURLs to add:")
        print("\n".join(urls))
        print("\nAPI Call Details:")
        print("Endpoint:", endpoint)
        print("Headers:", headers)
        print("Data:", json.dumps(data, indent=4))
        input("\nPress any key to continue...")

    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        print("URLs added successfully.")
    else:
        print("\nError in API response: ", response.text)

def remove_urls(api_token, chatbot_id, debug):
    """Remove URLs from the chatbot."""
    print("\nEnter URLs to remove (one URL per line, end with Ctrl+D):")
    urls = []
    while True:
        try:
            url = input()
            if validate_url(url):
                urls.append(url)
        except EOFError:
            break

    print("\nURLs to be removed:")
    for url in urls:
        print(url)

    confirm = input("\nDo you confirm removing these URLs? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Operation cancelled.")
        return

    endpoint = 'https://app.wonderchat.io/api/v1/delete-pages'
    headers = {'Content-Type': 'application/json'}
    data = {
        "apiKey": api_token,
        "chatbotId": chatbot_id,
        "urls": urls
    }
    if debug:
        print("\nURLs to remove:")
        print("\n".join(urls))
        print("\nAPI Call Details:")
        print("Endpoint:", endpoint)
        print("Headers:", headers)
        print("Data:", json.dumps(data, indent=4))        
        input("\nPress any key to continue...")
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        print("URLs removed successfully.")
    else:
        print("\nError in API response: ", response.text)

def reindex_urls(api_token, chatbot_id, debug):
    """Reindex URLs in the chatbot."""
    print("\nEnter URLs to reindex (one URL per line, end with Ctrl+D):")
    urls = []
    while True:
        try:
            url = input()
            if validate_url(url):
                urls.append(url)
        except EOFError:
            break

    print("\nURLs to be reindexed:")
    for url in urls:
        print(url)

    confirm = input("\nDo you confirm reindexing these URLs? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Operation cancelled.")
        return

    headers = {'Content-Type': 'application/json'}
    remove_endpoint = 'https://app.wonderchat.io/api/v1/delete-pages'
    add_endpoint = 'https://app.wonderchat.io/api/v1/add-pages'
    

    # Remove pages
    remove_endpoint = 'https://app.wonderchat.io/api/v1/delete-pages'
    remove_data = {
        "apiKey": api_token,
        "chatbotId": chatbot_id,
        "urls": urls
    }
    if debug:
        print("\nURLs to reindex:")
        print("\n".join(urls))
        print("\nAPI Call Details for Remove:")
        print("Endpoint:", remove_endpoint)
        print("Headers:", headers)
        print("Data:", json.dumps(remove_data, indent=4))
        input("\nPress any key to continue...")        
    remove_response = requests.post(remove_endpoint, headers=headers, json=remove_data)

    if remove_response.status_code == 200:
        print("Pages removed successfully.")
    else:
        print("\nError in API response while removing pages: ", remove_response.text)

    # Add pages
    add_endpoint = 'https://app.wonderchat.io/api/v1/add-pages'
    add_data = {
        "apiKey": api_token,
        "chatbotId": chatbot_id,
        "urls": urls
    }
    if debug:     
        print("\nAPI Call Details for Add:")
        print("Endpoint:", add_endpoint)
        print("Headers:", headers)
        print("Data:", json.dumps(add_data, indent=4))        
        input("\nPress any key to continue...")
    add_response = requests.post(add_endpoint, headers=headers, json=add_data)

    if add_response.status_code == 200:
        print("Pages reindexed successfully.")
    else:
        print("\nError in API response while reindexing pages: ", add_response.text)


def edit_configuration():
    """Edit the configuration."""
    api_token, chatbot_id, debug = load_config()
    
    print("\nCurrent Configuration:")
    print("API Token:", api_token)
    print("Chatbot ID:", chatbot_id)
    print("Debug Mode:", debug)

    new_api_token = input("\nEnter new API Token (leave blank to keep current value): ").strip()
    new_chatbot_id = input("Enter new Chatbot ID (leave blank to keep current value): ").strip()

    while True:
        new_debug = input("Enter new Debug Mode (True/False, leave blank to keep current value): ").strip().lower()
        if new_debug in ('true', 'false', ''):
            break
        else:
            print("Invalid input. Please enter 'True', 'False' or leave blank.")

    if new_api_token:
        api_token = new_api_token
    if new_chatbot_id:
        chatbot_id = new_chatbot_id
    if new_debug:
        debug = new_debug == 'true'

    save_config(api_token, chatbot_id, debug)
    print("\nNew Configuration Saved:")
    print("API Token:", api_token)
    print("Chatbot ID:", chatbot_id)
    print("Debug Mode:", debug)
    
    return api_token, chatbot_id, debug

def main():
    while True:
        api_token, chatbot_id, debug = load_config()

        if not api_token or not chatbot_id:
            print("Please configure your API token and chatbot ID using the 'Edit Configuration' option.")
            return

        print("\nWelcome to the WonderChat.ai Tool!")
        print("API Token:", api_token)
        print("Chatbot ID:", chatbot_id)
        print("Debug Mode:", debug)
        print("\nSelect an option:")
        print("1. Chat with Bot")
        print("2. Add URLs")
        print("3. Remove URLs")
        print("4. Reindex URLs")
        print("5. Edit Configuration")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            chat_with_bot(api_token, chatbot_id, debug)
        elif choice == '2':
            add_urls(api_token, chatbot_id, debug)
        elif choice == '3':
            remove_urls(api_token, chatbot_id, debug)
        elif choice == '4':
            reindex_urls(api_token, chatbot_id, debug)
        elif choice == '5':
            api_token, chatbot_id, debug = edit_configuration()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
