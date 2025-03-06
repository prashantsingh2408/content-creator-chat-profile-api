from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
import os
import chat_context_api

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/test_groq_get")
async def test_groq_get(query: str):
    try:
        response = chat_context_api.test_groq_get(query)
        return {
            "status": "success",
            "response": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
        
@app.post("/chat_content_api")
async def chat_content_api(user_message: str):
    try:
        response = chat_context_api.chat_content_api(user_message)
        return {
            "status": "success",
            "response": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    