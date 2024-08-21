import os
from azure_openai import OpenAI

class AzureOpenAIClient:
    """
    A client to interact with Azure OpenAI service.
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        self.client = OpenAI(api_key=self.api_key, endpoint=self.endpoint)

    def generate_response(self, prompt):
        """
        Generate a response from OpenAI based on the provided prompt.

        :param prompt: str: The input text prompt.
        :return: str: The generated response from OpenAI.
        """
        response = self.client.Completions.create(
            deployment_id=self.deployment_name,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

# Usage example:
# client = AzureOpenAIClient()
# response = client.generate_response("Hello, how are you?")
