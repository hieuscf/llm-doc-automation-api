from fastapi import FastAPI
from app.config.database import Base, engine
from app.routes.source_route import source_route
from app.routes.setting_route import setting_route

app = FastAPI(title="LLM Document automation api (Gemini API)")

@app.get("/")
def home():
    return {"message": "Welcome to LLM Document automation api using Gemini!"}

app.include_router(source_route)
app.include_router(setting_route)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)