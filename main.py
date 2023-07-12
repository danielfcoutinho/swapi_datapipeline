from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Params(BaseModel):
    url: str

@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.post("/dados")
def get_dados(params: Params):

    try:
        response = requests.get(params.url) # Here params is an instance of Params and url is a property of Params

        return response.json()

    except Exception as ex:
        raise HTTPException(status_code=ex.code, detail=f"{ex}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)