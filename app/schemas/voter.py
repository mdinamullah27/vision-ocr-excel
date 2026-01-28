from pydantic import BaseModel

class Voter(BaseModel):
    name: str
    voter_no: str
    father: str
    mother: str
    dob: str
    address: str
