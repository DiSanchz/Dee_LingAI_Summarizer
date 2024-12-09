import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class OpenAIAgent:
    def __init__(self, system_prompt, user_prompt, model="gpt-4o"):

        self.client = OpenAI()
        self.client.set_api_key(os.getenv("OPENAI_API_KEY"))

        self.model = model
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt

    def completion(self):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.user_prompt},
            ],
        )

        return completion.choices[0].message.content
