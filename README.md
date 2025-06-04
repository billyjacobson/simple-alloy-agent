# AlloyDB MCP ADK Example

This example demonstrates how to interact with an AlloyDB database using AI Agents with the Model Context Protocol (MCP) Database Toolbox and Google Agent Development Kit (ADK).

## Prerequisites

- [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) installed
- Access to an [AlloyDB instance](https://cloud.google.com/alloydb) on Google Cloud Platform
- [Gemini API key](https://aistudio.google.com/apikey) for accessing Google AI models
- Python 3.10 or newer
- [uv](https://github.com/astral-sh/uv) package manager

## Setup

1. Synchronize dependencies using uv:

    ```bash
    uv sync
    ```

2. Create the environment files:

    ```bash
    cp .env.example .env
    cp alloydb_agent/.env.example alloydb_agent/.env
    ```

3. Edit the `.env` files and fill in your credentials:
   - In the root `.env` file:
     - Fill in AlloyDB connection details (`ALLOYDB_PROJECT`, `ALLOYDB_REGION`, etc.)
   - In the `alloydb_agent/.env` file:
     - For Google AI API (default):
       - Set `GOOGLE_API_KEY` with your Gemini API key
     - OR for Vertex AI:
       - See the [ADK documentation](https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model) for complete Vertex AI setup instructions

4. Source the environment variables:

    ```bash
    source .env
    ```

5. Start the MCP Toolbox with the provided tools configuration:

    ```bash
    # Replace with the actual path to your MCP Toolbox executable
    /path/to/toolbox --tools-file "alloy-tools.yaml"
    ```

6. In a separate terminal, activate the virtual environment and start the ADK server:

    ```bash
    source .venv/bin/activate
    adk web
    ```

    The ADK web interface should now be available at http://localhost:8080, where you can interact with your AlloyDB database using natural language.