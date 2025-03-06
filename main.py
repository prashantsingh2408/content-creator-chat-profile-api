from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
import os
import chat_context_api

app = FastAPI()
      
@app.post("/chat_content_api")
async def chat_content_api(user_message: str):
    """
    Expected format: \n
    Request Body:
    user_message (str): 
        <CHAT> \n
        USER: hi \n
        </CHAT> \n
        <CONTENT> \n
        Profile: \n
        </CONTENT> \n

    Expected Response: \n
        <CHAT>   \n
        USER: Hi   \n
        BOT: Hi! How are you? What is your name?  \n
        </CHAT>  \n
        <CONTENT>  \n
        Profile:  \n
        </CONTENT>  \n
    """
    try:
        response = chat_context_api.chat_content_api(user_message)
        return {
            "status": "success",
            "response": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
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
  