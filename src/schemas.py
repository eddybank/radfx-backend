from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional, Set, Union
from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str

class Facility(BaseModel):
    name: str
    full_name: str
    description: str
    accelerator: str
    hours_of_operation: str

class Facilities(BaseModel):
    page: str
    per_page: str
    total_page: str
    total_count: str
    #data: []
        
    
class User(BaseModel):
    id: str
    affiliation_id: str
    user_name: str
    full_name: str
    first_name: str
    last_name: str
    created_at: str
    updated_at: str
    phone_number: str
    email: str
    verified_at: str
    disabled_at: str
    deleted_at: str
    role: str
    
class Users(BaseModel):
    page: str
    per_page: str
    total_page: str
    total_count: str
    #data: []

class Affiliation(BaseModel):
    id: str
    name: str
    full_name: str
    description: str
    #created_by: {}
    
class Affiliations(BaseModel):
    page: str
    per_page: str
    total_page: str
    total_count: str
    #data: []
    
class Project(BaseModel):
    id: str
    #created_by: {}
    project_name: str
    description: str
    program: str
    devices_under_test: str
    purpose_of_test: str
    total_hours: str
    vacuum: str
    status: str
    created_at: str
    updated_at: str
    submitted_at: str
    approved_at: str
    scheduled_at: str
    completed_at: str
    cancelled_at: str
    test_start: str
    test_end: str
    #requests: []
    is_public: str
    
class Projects(BaseModel):
    page: str
    per_page: str
    total_page: str
    total_count: str
    #data: []
    
class Request(BaseModel):
    id: str
    project_id: str
    facility_id: str
    energy_level: str
    ions: str
    integrator_id: str
    
class Requests(BaseModel):
    page: str
    per_page: str
    total_page: str
    total_count: str
    #data: []