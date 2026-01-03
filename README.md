# LLM-Powered Ticket Triage System

An AI-powered support ticket triage system using OpenAI's GPT model to categorize tickets and assign priorities. Outputs structured JSON for easy integration, validation, and storage.

## Features

- **LLM-Powered**: Uses GPT-3.5-turbo (or GPT-4) for intelligent classification
- **No Dataset Required**: Leverages pre-trained language model knowledge
- **No Keyword Rules**: AI understands context and nuance
- **Deterministic Output**: Temperature=0 ensures consistent results
- **Strict JSON Output**: Easy to validate, store, and extend
- **Categories**: technical, accounts, general
- **Priorities**: high, medium, low

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

Run the script interactively:

```bash
python ticket_triage.py
```

Or process a single ticket from command line:

```bash
python ticket_triage.py "My account login is broken and urgent!"
```

Enter ticket descriptions when prompted (interactive mode). Type 'quit' to exit.

Example output:

```json
{
  "category": "accounts",
  "priority": "high"
}
```

## Requirements

- Python 3.x
- OpenAI API key
- `openai` Python package

## How It Works

The system sends each ticket to OpenAI's GPT model with a structured prompt that defines the categories and priorities. The model responds with a JSON object containing the classification results. This approach provides:

- **Contextual Understanding**: Goes beyond simple keywords
- **Consistency**: Deterministic responses with temperature=0
- **Extensibility**: Easy to add new categories or priorities by modifying the prompt
- **Validation**: JSON format ensures structured, parseable output

## Customization

To change categories or priorities, modify the prompt in the `triage_ticket` function. For example, add more categories or adjust priority criteria.
