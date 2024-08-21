from utils.helpers import format_response

def test_format_response():
    assert format_response("  hello world ") == "Hello world", "Formatted response is incorrect."
