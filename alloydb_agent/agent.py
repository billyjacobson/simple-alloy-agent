from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox_client = ToolboxSyncClient("http://127.0.0.1:5000")

prompt = "You're a helpful database assistant with the ability to read data from a table."

root_agent = Agent(
    model='gemini-2.0-flash',
    name='database_agent',
    description='A helpful AI assistant.',
    instruction=prompt,
    tools=toolbox_client.load_toolset("my-toolset"),
)