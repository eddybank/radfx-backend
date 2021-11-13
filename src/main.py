from fastapi import FastAPI, Depends, HTTPException
from .auth import AuthHandler
from .schemas import AuthDetails, Facility
from .dummy_models import facility as demo_facility
from .dummy_models import facilities as demo_facilities
from .dummy_models import user as demo_user
from .dummy_models import users as demo_users
from .dummy_models import affilitation as demo_affilitation
from .dummy_models import affilitations as demo_affilitations
from .dummy_models import project as demo_project
from .dummy_models import projects as demo_projects
from .dummy_models import request as demo_request
from .dummy_models import requests as demo_requests


app = FastAPI()


auth_handler = AuthHandler()
users = []
projects = []
requests = []
affiliations = []
facilities = []


@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password    
    })
    return


@app.post('/login')
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break
    
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return { 'token': token }


@app.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }


@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }


@app.post('/facility')
def post_facility(response_details: Facility):
    facilities.append({
        'name': response_details.name,
        'full_name': response_details.full_name,
        'description': response_details.description,
        'accelerator': response_details.accelerator
    })
    return facilities


@app.get('/facility')
def facility():
    return demo_facility


@app.get('/facilities')
def get_facilities():
    return facilities 


@app.get('/user')
def user():
    return demo_user


@app.get('/users')
def users():
    return demo_users


@app.get('/affilitation')
def affilitation():
    return demo_affilitation


@app.get('/affilitations')
def affilitations():
    return demo_affilitations


@app.get('/project')
def project():
    return demo_project


@app.get('/projects')
def projects():
    return demo_projects


@app.get('/request')
def request():
    return demo_request


@app.get('/requests')
def requests():
    return demo_requests