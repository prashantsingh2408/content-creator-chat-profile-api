from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from groq import Groq
import os

# Load environment variables
load_dotenv()

# Initialize the FastAPI app and Groq client
app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Root endpoint to return a greeting message
@app.get("/")
async def root():
    return {"status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/test-groq")
async def test_groq():
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": "Explain the importance of fast language models"
            }],
            temperature=0.7,
            max_tokens=1024
        )
        
        return {
            "status": "success",
            "response": completion.choices[0].message.content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

'''
GET /chat?query=What is the capital of France?
'''
@app.get("/chat")
async def chat(query: str):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": query
            }],
            temperature=0.7,
            max_tokens=1024
        )
        
        return {
            "status": "success",
            "response": completion.choices[0].message.content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))