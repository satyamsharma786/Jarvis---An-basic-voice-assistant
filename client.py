import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key=os.getenv("NEWS_API_KEY")
print("api key loaded:",bool(api_key))
if api_key:
    print("api key is configured")
else:
    print("api key is not configured")


# client = OpenAI(api_key=api_key)

# response = client.responses.create(
#     model="gpt-5.6",
#     input="Write a one-sentence bedtime story about a unicorn.",
# )

# print(response.output_text)