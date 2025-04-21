from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import (MCPToolset,
                                                   StdioServerParameters)

load_dotenv('../.env')

# --- Step 1: Import Tools from MCP Server ---
async def get_tools_async():
  print("Attempting to connect to MCP Blender server...")
  tools, exit_stack = await MCPToolset.from_server(
      connection_params=StdioServerParameters(
          command='uvx', # Command to run the server
          args=["blender-mcp"],
      )
  )
  print("MCP Toolset created successfully.")
  return tools, exit_stack

# --- Step 2: Agent Definition ---
async def get_agent_async():
  tools, exit_stack = await get_tools_async()
  print(f"Fetched {len(tools)} tools from MCP server.")
  root_agent = LlmAgent(
      model=LiteLlm(model='anthropic/claude-3-7-sonnet-20250219'),
      name='blender_assistant',
      instruction='Help user interact with the blender using available tools.',
      tools=tools, # Provide the MCP tools to the ADK agent
  )
  return root_agent, exit_stack

root_agent = get_agent_async()
