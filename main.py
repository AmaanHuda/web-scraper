"""
Website summarizer using gemini instead of OpenAI.
"""

from openai import OpenAI
from scraper import fetch_website_contents
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL = "gemini-2.5-flash-lite"
key = os.getenv("GOOGLE_API_KEY")

print(key)
system_prompt = """
You are a nerdy assistant that looks deep into things and tries to make everything you see easy to understand. You are like a detective which will note down all the small important details you see. You will ignore all the things which are navigation related or not very important and give out only the things that are the most important.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""


def messages_for(website):
    """Create message list for the LLM."""
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]


def summarize(url):
    """Fetch and summarize a website using gemini."""
    gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=key)
    website = fetch_website_contents(url)
    response = gemini.chat.completions.create(
        model=MODEL,
        messages=messages_for(website)
    )
    return response.choices[0].message.content


def main():
    """Main entry point for testing."""
    
    url = input("Enter a URL to summarize: ")

    if url.startswith("https://") or url.startswith("http://"):
        print("\nFetching and summarizing...\n")
        summary = summarize(url)
        print(summary)

    else:
        print("Please enter a valid link")
        main()


main()
