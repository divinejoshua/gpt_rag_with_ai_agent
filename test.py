from decouple import config
import os

# llama index requires the os.environ variable called OPENAI_API_KEY:
os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo", api_key="BAD_KEY")
resp = OpenAI().complete("Paul Graham is ")
print(resp)