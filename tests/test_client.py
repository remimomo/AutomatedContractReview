import pytest
from azure_openai.client import AzureOpenAIClient

@pytest.fixture
def openai_client():
    return AzureOpenAIClient()

def test_generate_response(openai_client, mocker):
    mocker.patch.object(openai_client.client.Completions, 'create', return_value={
        'choices': [{'text': 'This is a test response'}]
    })

    response = openai_client.generate_response("Test prompt")
    assert response == "This is a test response", "Response does not match expected output."
