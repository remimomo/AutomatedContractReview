from langchain import LLMChain
from langchain.prompts import PromptTemplate
from azure_openai.client import AzureOpenAIClient

def get_openai_response(user_input):
    """
    Get a response from the OpenAI model using the Langchain pipeline.

    :param user_input: str: The user's input query.
    :return: str: The generated response.
    """
    # Initialize the Azure OpenAI client
    openai_client = AzureOpenAIClient()

    # Create a Langchain template
    template = PromptTemplate(input_variables=["input"], template="Your prompt: {input}")

    # Create a Langchain pipeline
    chain = LLMChain(llm=openai_client, prompt=template)

    # Run the pipeline with the user input
    result = chain.run(user_input)
    
    return result
