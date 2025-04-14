from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import pdb; pdb.set_trace()
model = OllamaLLM(model='hf.co/bartowski/granite-3.0-1b-a400m-instruct-GGUF:latest')
template = """
You are question answering system that can perform operations
and perform required operations

Here is the repository I want you to clone when I say get repo {repo} by running
git clone 
Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)