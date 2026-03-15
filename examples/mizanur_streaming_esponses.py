"""
Streaming Responses Example
============================

Demonstrates streaming responses for better user feedback.
Shows how to get real-time output as the model generates text.

Run with:
    python examples/streaming_responses.py
"""

from dotenv import load_dotenv
load_dotenv()

from orchestral import Agent
from orchestral.llm import Ollama

agent = Agent(
    llm=Ollama(model="gpt-oss:120b-cloud"),
    system_prompt="You are a helpful coding assistant."
)

print("Streaming response from agent:\n")
print("-" * 60)

# Stream the response token by token
for chunk in agent.stream_text_message("Write a Python function to calculate fibonacci numbers."):
    print(chunk, end='', flush=True)

print("\n" + "-" * 60)
print("\nStreaming complete!")