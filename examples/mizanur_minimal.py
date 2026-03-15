from dotenv import load_dotenv
load_dotenv()

from orchestral import Agent
from orchestral.llm import Ollama
from orchestral.ui.app import server as app_server

agent = Agent(llm=Ollama(model="gpt-oss:120b-cloud"))
app_server.run_server(agent)