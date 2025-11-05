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
    description="Sistema Multi-Agente para Agricultura Inteligente",
    version="1.0.0"
)

# ========== CORS CONFIGURATION (CRÍTICO!) ==========
# IMPORTANTE: allow_credentials DEVE ser False quando allow_origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite TODAS as origens
    allow_credentials=False,  # OBRIGATÓRIO: False quando usa ["*"]
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, OPTIONS, etc)
    allow_headers=["*"],  # Permite todos os headers
    expose_headers=["*"]  # Expõe todos os headers na resposta
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


@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    """Handle OPTIONS requests for CORS preflight."""
    from fastapi.responses import Response
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, PATCH",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Max-Age": "3600",
        }
    )


# Adicionar middleware adicional para garantir CORS em todas as respostas
@app.middleware("http")
async def add_cors_header(request, call_next):
    """Adiciona headers CORS em todas as respostas."""
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, PATCH"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )

