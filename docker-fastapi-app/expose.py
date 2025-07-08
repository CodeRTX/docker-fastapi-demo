from pyngrok import ngrok

# Set your ngrok authtoken (replace 'your_ngrok_authtoken_here' with your actual authtoken)
ngrok.set_auth_token("NGROK_AUTHTOKEN")

# Open a tunnel to the FastAPI application running on port 8000
public_url = ngrok.connect(8000)
print(f"Public URL: {public_url}")
