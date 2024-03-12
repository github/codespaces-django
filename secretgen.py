from django.core.management.utils import get_random_secret_key

# Generate a random secret key
secret_key = get_random_secret_key()
print("please copy this code and replace it in your .env file secret key")
print(secret_key)
    
