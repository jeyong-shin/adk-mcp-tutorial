import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool


load_dotenv('../.env')

# --- Step 1: Import Tools from MCP Server ---
async def get_tools_async():
  """Gets tools from the Obsidian MCP Server."""
  print("Attempting to connect to MCP Obsidian server...")
  tools, exit_stack = await MCPToolset.from_server(
      # Use StdioServerParameters for local process communication
      connection_params=StdioServerParameters(
          command='uvx', # Command to run the server
          args=[
                "mcp-obsidian",
                ],
          env={
            "OBSIDIAN_API_KEY": os.environ["OBSIDIAN_API_KEY"],
            "OBSIDIAN_HOST": os.environ["OBSIDIAN_HOST"],
          }
      )
  )
  print("MCP Toolset created successfully.")
  return tools, exit_stack

# --- Step 2: Agent Definition ---
async def get_agent_async():
  """Creates an ADK Agent equipped with tools from the MCP Server."""
  tools, exit_stack = await get_tools_async()
  print(f"Fetched {len(tools)} tools from MCP server.")

  search_tool = LlmAgent(
    model='gemini-2.5-flash-preview-04-17',
    name='google_search_agent',
    instruction='Help user search the web using Google Search.',
    tools=[google_search], # Provide the MCP tools to the ADK agent
  )

  root_agent = LlmAgent(
      model='gemini-2.5-flash-preview-04-17',
      name='obsidian_assistant',
      instruction='Help user interact with the obsidian using available tools.',
      tools=tools + [AgentTool(agent=search_tool)],
  )
  return root_agent, exit_stack

root_agent = get_agent_async()
