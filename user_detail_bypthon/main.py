from fastapi import FastAPI
import uvicorn
#from mysqlquery.mysql_query_util import get_connection,get_table_data
from routes import department_router

app=FastAPI(title="User Management Service")

app.include_router(department_router.loadDepartmentrouter)
app.include_router(department_router.createDepartmentrouter)


@app.get("/")
def root():
    return {"message":"User management service is running"}

if __name__=="__main__":

    print("starting server at port:8000")
    
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
    
    