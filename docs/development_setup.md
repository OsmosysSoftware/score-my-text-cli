# Development Setup

## Prerequisites

To setup and use Score My Text CLI, you need to have Python installed on your system. Additionally, you'll require an OpenAI API key. If you don't have one, you can sign up for an API key on the OpenAI platform.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone git@github.com:OsmosysSoftware/score-my-text-cli.git
   cd score-my-text-cli
   ```

2. Create a virtual environment (venv) for the evaluator. Replace second `venv` with your preferred environment name:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   After activation, your command prompt should show the virtual environment's name, indicating that it's active.

4. Install the required packages within the virtual environment using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install the necessary packages, including the `openai` package.

5. Configure `.env` file

   Create a `.env` file using the provided `.env.example` file, and add your OpenAI API Key to it.

## Deactivating Virtual Environment

When you're finished using Score My Text CLI, deactivate the virtual environment:

- On Windows:

  ```bash
  deactivate
  ```

- On macOS and Linux:

  ```bash
  deactivate
  ```

This ensures that dependencies are isolated and won't interfere with your system's global Python environment.
