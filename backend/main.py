from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import asyncio
import json
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="ASX Real-Time Analytics", 
    version="1.0.0",
    description="Real-time Australian Stock Exchange analytics with economic indicators"
)

# Security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "*.herokuapp.com", "*.vercel.app"]
)

# CORS middleware
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "ASX Real-Time Analytics API", "status": "active"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "asx-analytics"}

@app.get("/api/stocks")
async def get_stocks():
    """Get sample ASX stock data"""
    sample_stocks = [
        {"code": "CBA", "name": "Commonwealth Bank", "price": 142.50, "change": 1.2},
        {"code": "BHP", "name": "BHP Group", "price": 45.80, "change": -0.5},
        {"code": "CSL", "name": "CSL Limited", "price": 285.30, "change": 2.1}
    ]
    return {"stocks": sample_stocks}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)