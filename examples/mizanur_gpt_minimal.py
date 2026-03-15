from dotenv import load_dotenv
load_dotenv()

from orchestral import Agent
from orchestral.llm import GPT
from orchestral.ui.app import server as app_server

agent = Agent(llm=GPT(model="gpt-4o"))
app_server.run_server(agent)