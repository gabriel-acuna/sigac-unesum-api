import uvicorn
from decouple import config

if __name__ =='__main__':

    uvicorn.run("app.api.routes:app", host="0.0.0.0",port=int(config("PORT")), reload=True)