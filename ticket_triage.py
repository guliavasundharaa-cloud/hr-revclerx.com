#!/usr/bin/env python3
import os
import json
import requests

# Set your API key (replace with your actual key)
os.environ["GROK_API_KEY"] = "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"  # Replace with your real key

# API URL for the Groq OpenAI endpoint
GROK_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def explain_importance_of_fast_language_models() -> dict:
    # Payload data with the exact structure you provided
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": "account is not working ticket triage"
            },
            {
                "role": "system",
                "content": "you are llm based support ticket triage system. which should accept support text as input and use llm to classify category of ticket and prioority low medium high and extract information from input to suggest next steps to resolve the ticket.  respond in json format with keys category , priority and next_steps. category should be one of billing, technical support, account management, general inquiry. priority should be low medium high. next_steps should be a list of steps to resolve the ticket."
            }
        ]
    }

    # Set headers for the API request
    headers = {
        "Authorization": f"Bearer {os.getenv('GROK_API_KEY')}",
        "Content-Type": "application/json"
    }

    try:
        # Send the POST request to the API
        response = requests.post(GROK_API_URL, headers=headers, json=data)

        # If the request is successful, return the response
        if response.status_code == 200:
            return response.json()
        else:
            # Handle failure case with status code and error message
            return {
                "error": f"Request failed with status {response.status_code}: {response.text}"
            }
    except Exception as e:
        # Handle any exception that occurs during the request
        return {
            "error": str(e)
        }

if __name__ == "__main__":
    # Inform the user the request is being processed
    print("Requesting explanation on the importance of fast language models...")
    
    # Call the function to get the result
    result = explain_importance_of_fast_language_models()
    
    # Print the result as formatted JSON
    print(json.dumps(result, indent=2))

