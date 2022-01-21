# FastAPI JWT Auth

## Getting Started
If using windows be sure to open your VSCode editor with administrator privileges first or you will get an 'access denied error

Set up a virtual environment for the project:  
`python3 -m venv virtualenv`

Activate the environment:  
`virtualenv/Scripts/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Run the API with Uvicorn:  
`uvicorn src.main:app --reload`

Hit the unprotected endpoint with cURL:  
`curl localhost:8000/unprotected`

Hit the protected endpoint with cURL to get a 403:  
`curl localhost:8000/protected`

Register a user:  
`curl -H "Content-Type: application/json" -X POST http://localhost:8000/register -d "{\"username\": \"eddy\", \"password\": \"bank\"}"`

Log in and get a token:  
`curl -H "Content-Type: application/json" -X POST http://localhost:8000/login -d "{\"username\": \"eddy\", \"password\": \"bank\"}"`

Then use that token as an auth header to get a valid response from the protected endpoint:  
`curl --header "Authorization: Bearer <TOKEN>" localhost:8000/protected`
