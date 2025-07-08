import os
from pyngrok import ngrok

load_dotenv()  # Loads the .env file into environment variables

# Set your ngrok authtoken (use your actual auth-token)
auth_token = os.getenv("NGROK_AUTHTOKEN")
ngrok.set_auth_token(auth_token)

# Open a tunnel to the FastAPI application running on port 8000
public_url = ngrok.connect(8000)
print(f"Public URL: {public_url}")
