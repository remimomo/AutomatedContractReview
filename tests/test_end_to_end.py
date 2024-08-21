import pytest
from streamlit.testing import StreamlitRunner
from app import app  # Assuming the main Streamlit app is defined in app.py

@pytest.fixture
def mock_pipeline(mocker):
    # Mocking the Azure OpenAI response within the pipeline
    mocker.patch('langchain.LLMChain.run', return_value="This is a mocked response")

def test_end_to_end(mock_pipeline):
    """
    End-to-end test simulating a user entering a query in the Streamlit UI
    and receiving a processed response.
    """
    # Initialize Streamlit test runner
    runner = StreamlitRunner(app)

    # Simulate entering user input
    runner.input("Enter your query:", "Test input")

    # Run the Streamlit app
    result = runner.run()

    # Check that the correct response is displayed
    assert "This is a mocked response" in result, "The response does not match the expected output."
