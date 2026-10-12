from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
import anthropic
from anthropic import Anthropic
from claude_api_utils import (
    add_user_message,
    add_assistant_message,
    chat,
    text_from_message,
)

load_dotenv(override=True)
console = Console()

client = Anthropic()
MODEL = "claude-haiku-4-5-20251001"  # or "claude-sonnet-4-5"

console.print(f"[yellow]Using Anthropic API: [/yellow] {anthropic.__version__}")

messages = []

SYSTEM_PROMPT = """
    You are a helpful assistant that answers questions briefly and too the point.
    Response from your training data only. If you do not know the answer, say "I don't know" and do not make up an answer. Always respond in Markdown format.
"""

add_user_message(
    messages,
    "What should I search to find the latest development in Claude and Claude Code?",
)

response = chat(
    client=client,
    model=MODEL,
    messages=messages,
    system_prompt=SYSTEM_PROMPT,
)

response_text = text_from_message(response)
# for block in response.content:
#     if block.type == "text":
#         response_text += block.text

console.print(f"[green]AI:[/green]\n {response_text}")
