import os
from fastapi import HTTPException, APIRouter
import logging
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from .models import ChatRequest, ChatResponse
load_dotenv()
# Configure logging
logger = logging.getLogger(__name__)

# Get Ollama base URL from environment variable or use default
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")

chat_router = APIRouter(prefix="/llm", tags=["llm"])

@chat_router.get("/")
async def read_root():
    return {"message": "Welcome to the Chat API"}


@chat_router.get("/models")
async def list_models():
    try:
        # For now, just return the default model we're using
        return {"models": ["gemma3:1b-it-q4_K_M"]}
    except Exception as e:
        logger.error(f"Error listing models: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error listing models: {str(e)}")


@chat_router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        logger.info(f"Processing chat request with model: {request.model}")
        
        # Initialize the LLM
        llm = ChatOllama(
            model=request.model,
            base_url=OLLAMA_BASE_URL,
            temperature=request.temperature,
        )
        
        # Convert request messages to langchain format
        langchain_messages = []
        for msg in request.messages:
            if msg.role == "system":
                langchain_messages.append(("system", msg.content))
            elif msg.role == "human":
                langchain_messages.append(("human", msg.content))
            elif msg.role == "ai":
                langchain_messages.append(("ai", msg.content))
        
        # Get response from the model
        ai_msg = llm.invoke(langchain_messages)
        
        return ChatResponse(content=ai_msg.content)
    
    except Exception as e:
        logger.error(f"Error processing chat: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")
