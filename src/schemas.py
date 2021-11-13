from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str

class Facility(BaseModel):
    name: str
    full_name: str
    description: str
    accelerator: str
