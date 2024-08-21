#!/bin/bash

# Create and activate virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Print success message
echo "Environment setup complete. Run 'streamlit run app.py' to start the application."
