from fastapi import APIRouter
from services.services_department_mgmt import findAlldepartment,saveDepartmentDetail
from schema.schema_departmentdetails import CreateDepartment

loadDepartmentrouter=APIRouter(prefix="/departments",tags=["Department Fetching"])

createDepartmentrouter=APIRouter(prefix="/createdepartments",tags=["Create department"])



@loadDepartmentrouter.get("/",status_code=200)
def fetch_departments():
    result=findAlldepartment()
    print("inrouter",result)
    return result

@createDepartmentrouter.post("/",status_code=200)
def create_department(crateObj:CreateDepartment):
    result=saveDepartmentDetail(crateObj)
    return result

