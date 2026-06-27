import os

print("DATABASE_URL:", os.getenv("DATABASE_URL"))
print("All environment variables:")
print(dict(os.environ))