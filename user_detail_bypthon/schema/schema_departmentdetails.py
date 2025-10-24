from pydantic import BaseModel

class CreateDepartment(BaseModel):
    departmentId:int
    departmentAddress:str
    departmentCode:str
    departmentName:str
