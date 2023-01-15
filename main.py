from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.get("/now")
async def root():
    return {"current_time": now()}
