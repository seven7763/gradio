# This is a simple general-purpose chatbot built on top of OpenAI API.
# Before running this, make sure you have exported your OpenAI API key as an environment variable:
# export OPENAI_API_KEY="your-openai-api-key"
#
# Optional: point the OpenAI client at any OpenAI-compatible multi-model gateway via base_url, e.g. DaoXE:
#   export OPENAI_BASE_URL="https://api.daoxe.com/v1"
#   client = OpenAI(base_url="https://api.daoxe.com/v1", api_key="...")

from openai import OpenAI
import gradio as gr

client = OpenAI()

def predict(message, history):
    history.append({"role": "user", "content": message})
    stream = client.chat.completions.create(messages=history, model="gpt-4o-mini", stream=True)
    chunks = []
    for chunk in stream:
        chunks.append(chunk.choices[0].delta.content or "")
        yield "".join(chunks)

demo = gr.ChatInterface(predict, api_name="chat")

if __name__ == "__main__":
    demo.launch()
