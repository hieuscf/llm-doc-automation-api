from fastapi import FastAPI

app = FastAPI(title="LLM Document automation api (Gemini API)")

@app.get("/")
def home():
    return {"message": "Welcome to LLM Document automation api using Gemini!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)