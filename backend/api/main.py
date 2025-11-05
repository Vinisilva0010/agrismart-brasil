"""
AgriSmart Brasil - FastAPI Main Application
Multi-Agent System for Smart Agriculture
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from .routes import router

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="AgriSmart Brasil API",
    description="Multi-Agent System for Smart Agriculture using Google ADK",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Configure CORS - Permitir frontend em produção e desenvolvimento
cors_origins = os.getenv("CORS_ORIGINS", "*")
if cors_origins == "*":
    # Em produção sem CORS_ORIGINS configurado, permitir tudo
    allowed_origins = ["*"]
else:
    allowed_origins = cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False if "*" in allowed_origins else True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "AgriSmart Brasil API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/api/docs",
        "agents": [
            "climate_monitor",
            "crop_analyzer",
            "water_optimizer",
            "yield_predictor",
            "farm_manager"
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for Cloud Run."""
    return {
        "status": "healthy",
        "service": "agrismart-brasil"
    }


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )

