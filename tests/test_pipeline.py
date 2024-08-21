import pytest
from langchain_pipeline.pipeline import get_openai_response

@pytest.fixture
def mock_pipeline(mocker):
    mocker.patch('langchain.LLMChain.run', return_value="Mocked response")

def test_get_openai_response(mock_pipeline):
    response = get_openai_response("Test input")
    assert response == "Mocked response", "Pipeline response does not match expected output."
