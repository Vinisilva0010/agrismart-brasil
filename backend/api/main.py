"""
AgriSmart Brasil - FastAPI Main Application
Multi-Agent System for Smart Agriculture
"""

import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from dotenv import load_dotenv

from .routes import router

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="AgriSmart Brasil API",
    description="Sistema Multi-Agente para Agricultura Inteligente",
    version="1.0.0"
)

# ========== MIDDLEWARE HTTP PARA CORS (PRIMEIRO!) ==========
@app.middleware("http")
async def cors_middleware(request: Request, call_next):
    """Middleware para adicionar headers CORS em TODAS as requisições."""
    # Handle preflight OPTIONS requests
    if request.method == "OPTIONS":
        response = Response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, PATCH, HEAD"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Max-Age"] = "3600"
        return response
    
    # Process normal requests
    response = await call_next(request)
    
    # Add CORS headers to all responses
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, PATCH, HEAD"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Expose-Headers"] = "*"
    
    return response

# ========== CORS MIDDLEWARE (SEGUNDO!) ==========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# ========== OPTIONS HANDLER PARA TODAS AS ROTAS ==========
@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    """Handle OPTIONS requests for CORS preflight."""
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, PATCH, HEAD",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Max-Age": "3600",
        }
    )

# Include routers AFTER CORS setup
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
