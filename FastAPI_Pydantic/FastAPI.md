# API:
API is a way of two programmes to talk to each other. Your frontend  sends a request your backend sends back data.

# REST:
Arrest a set of rules for designing APIs. Uses http methods to perform actions:
GET→ retrieve data (read)
POST→ create new data
PUT→ update existing data
DELETE→ remove data

# Install:
pip install fastapi FastAPI

# Run:
uvicorn filename:app --reload

# What is Uvicorn and why does FastAPI need it?
A: Uvicorn is an ASGI server that actually runs the FastAPI application and handles incoming HTTP requests. FastAPI itself just defines the routes — Uvicorn serves them.