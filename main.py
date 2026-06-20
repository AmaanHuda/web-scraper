import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI


# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
else:
    print("API key found and looks good so far!")


message = "Hello, GPT! This is my first ever message to you! Hi!"
messages = [{"role": "user", "content": message}]

openAI = OpenAI(api_key=f"{api_key}")

response = openAI.chat.completions.create(model="gpt-5",messages=messages)
response.choice[0].message.content