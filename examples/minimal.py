"""
Minimal Orchestral Example
==========================

This is the absolute minimum code needed to run Orchestral.
Creates an agent with default settings and launches a web interface.

Run with:
    python examples/minimal.py

Then open http://127.0.0.1:8000 in your browser.
"""

from orchestral import Agent
import app.server as app_server

agent = Agent()
app_server.run_server(agent)
