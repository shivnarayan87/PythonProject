from mysqlquery.mysql_query_util import get_all_department,save_department
from schema.schema_departmentdetails import CreateDepartment

def findAlldepartment():
    resultObj=get_all_department()
    print(resultObj)
    return resultObj

def saveDepartmentDetail(departmentObj:CreateDepartment):
    save_department(departmentObj.departmentId,departmentObj.departmentName,departmentObj.departmentCode,departmentObj.departmentAddress)
    return {"status ": "department created"} 

   




# if __name__ == "__main__":
#     findAlldepartment()

