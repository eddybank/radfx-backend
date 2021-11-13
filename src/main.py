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


@app.post('/register', status_code=200)
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


@app.post('/facility', status_code=200)
def post_facility(response_details: Facility):
    facilities.append({
        'name': response_details.name,
        'full_name': response_details.full_name,
        'description': response_details.description,
        'accelerator': response_details.accelerator
    })
    return

@app.post('/facilities', status_code=200)
def post_facilities(response_details: Facilities):
    facilities.append({
        'page': response_details.page,
        'per_page': response_details.per_page,
        'total_page': response_details.total_page,
        'total_count': response_details.total_count
    })
    return

@app.post('/user', status_code=200)
def post_user(response_details: User):
    user.append({
        'id': response_details.id,
        'affiliation_id': response_details.per_page,
        'user_name': response_details.user_name,
        'full_name': response_details.full_name,
        'last_name': response_details.last_name,
        'created_at': response_details.created_at,
        'updated_at': response_details.updated_at,
        'phone_number': response_details.phone_number,
        'email': response_details.email,
        'verified_at': response_details.verified_at,
        'disabled_at': response_details.disabled_at,
        'deleted_at': response_details.deleted_at,
        'role': response_details.role
    })
    return

@app.post('/users', status_code=200)
def post_users(response_details: Users):
    users.append({
        'page': response_details.page,
        'per_page': response_details.per_page,
        'total_page': response_details.total_page,
        'total_count': response_details.total_count
    })
    return

@app.post('/affiliation', status_code=200)
def post_affiliation(response_details: Affiliation):
    affiliation.append({
        'id': response_details.id,
        'name': response_details.name,
        'full_name': response_details.full_name,
        'description': response_details.description
    })
    return

@app.post('/affiliations', status_code=200)
def post_affiliations(response_details: Affiliations):
    affiliations.append({
        'page': response_details.page,
        'per_page': response_details.per_page,
        'total_page': response_details.total_page,
        'total_count': response_details.total_count
    })
    return

@app.post('/project', status_code=200)
def post_project(response_details: Project):
    project.append({
        'id': response_details.id,
        'project_name': response_details.project_name,
        'description': response_details.description,
        'program': response_details.program,
        'devices_under_test': response_details.devices_under_test,
        'purpose_of_test': response_details.purpose_of_test,
        'total_hours': response_details.total_hours,
        'vacuum': response_details.vacuum,
        'status': response_details.status,
        'created_at': response_details.created_at,
        'updated_at': response_details.updated_at,
        'submitted_at': response_details.submitted_at,
        'approved_at': response_details.approved_at,
        'completed_at': response_details.completed_at,
        'cancelled_at': response_details.cancelled_at,
        'test_start': response_details.test_start,
        'test_end': response_details.test_end,
        'is_public': response_details.is_public
    })
    return

@app.post('/projects', status_code=200)
def post_projects(response_details: Projects):
    projects.append({
        'page': response_details.page,
        'per_page': response_details.per_page,
        'total_page': response_details.total_page,
        'total_count': response_details.total_count,
        'project_name': response_details.project_name,
        'description': response_details.description,
        'program': response_details.program,
        'devices_under_test': response_details.devices_under_test,
        'purpose_of_test': response_details.purpose_of_test,
        'total_hours': response_details.total_hours,
        'vacuum': response_details.vacuum,
        'is_public': response_details.is_public,
        'status': response_details.status,
        'created_at': response_details.created_at,
        'updated_at': response_details.updated_at,
        'submitted_at': response_details.submitted_at,
        'approved_at': response_details.approved_at,
        'scheduled_at': response_details.scheduled_at,
        'completed_at': response_details.completed_at,
        'cancelled_at': response_details.cancelled_at,
        'test_start': response_details.test_start,
        'test_end': response_details.test_end
    })
    return

@app.post('/request', status_code=200)
def post_request(response_details: Request):
    request.append({
        'id': response_details.id,
        'project_id': response_details.project_id,
        'facility_id': response_details.facility_id,
        'energy_level': response_details.energy_level,
        'ions': response_details.ions,
        'integrator_id': response_details.integrator_id
    })
    return

@app.post('/requests', status_code=200)
def post_requests(response_details: Requests):
    requests.append({
        'page': response_details.page,
        'per_page': response_details.per_page,
        'total_page': response_details.total_page,
        'total_count': response_details.total_count
    })
    return

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