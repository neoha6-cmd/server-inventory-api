from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
server= {

 1: {"id":3, "name": "web-01", "ip": "192.168.1.1", "env":"prod"},

 2: {"id":2, "name": "web-2", "p": "192.168.1.2", "env":"test"}

}
class NewServer(BaseModel):
    name: str
    ip: str
    env: str = "dev"
app=FastAPI()

@app.get("/server")
def list_server():
    return list(server.values())




@app.post("/server", status_code=201)
def create_server(new_server: NewServer):
    new_id = max(server.keys(), default=0) + 1
    server={
        "id": new_id,
        "name":new_server.name, 
        "ip":new_server.ip,
        "env": new_server.env
    }

    server[new_id]= server
    return server
@app.delete("/server{server_id}")
def delete_sever(server_id:int):
    if server_id not in server:
        raise HTTPException(status_code=404,detail=f"server {server_id} not found")
    deleted = server.pop(server_id)
    print(f"DELETE /server/{server_id} -> removed {deleted['name']}")
    return {"deleted":deleted}
