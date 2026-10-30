from fastapi import FastAPI
from routers import news
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 挂载路由/注册路由
app.include_router(news.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)