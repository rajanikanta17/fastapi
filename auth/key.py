import secrets

SECRET_KEY = secrets.token_hex(32)  # Generate a random secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

print(f"Generated SECRET_KEY: {SECRET_KEY}")  # Print the generated secret key for reference