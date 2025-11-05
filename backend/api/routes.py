"""
AgriSmart Brasil - API Routes
All endpoints for the multi-agent agriculture system
"""

from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
import base64
import io

from agents import (
    ClimateMonitorAgent,
    CropAnalyzerAgent,
    WaterOptimizerAgent,
    YieldPredictorAgent,
    FarmManagerAgent
)

router = APIRouter()

# Initialize agents
climate_agent = ClimateMonitorAgent()
crop_agent = CropAnalyzerAgent()
water_agent = WaterOptimizerAgent()
yield_agent = YieldPredictorAgent()
farm_manager = FarmManagerAgent()


# Pydantic models for request/response validation
class ClimateAnalysisRequest(BaseModel):
    location: str
    climate_data: Dict[str, Any]


class IrrigationRecommendationRequest(BaseModel):
    climate_data: Dict[str, Any]
    crop_type: str


class WeatherImpactRequest(BaseModel):
    forecast_data: Dict[str, Any]
    crop_stage: str


class CropImageAnalysisRequest(BaseModel):
    image_data: str
    crop_type: str
    additional_info: Optional[str] = None


class DiseaseIdentificationRequest(BaseModel):
    symptoms: str
    crop_type: str


class NutrientAssessmentRequest(BaseModel):
    observations: Dict[str, Any]
    crop_type: str


class CropRotationRequest(BaseModel):
    current_crop: str
    soil_condition: str
    previous_crops: List[str]


class IrrigationScheduleRequest(BaseModel):
    crop_type: str
    field_size: float
    soil_type: str
    climate_data: Dict[str, Any]
    water_availability: str


class WaterEfficiencyRequest(BaseModel):
    water_used: float
    field_size: float
    crop_yield: float
    crop_type: str


class IrrigationIssuesRequest(BaseModel):
    sensor_data: Dict[str, Any]
    irrigation_system: str


class IrrigationTechnologyRequest(BaseModel):
    farm_details: Dict[str, Any]
    budget: str
    water_source: str


class YieldPredictionRequest(BaseModel):
    crop_type: str
    field_size: float
    planting_date: str
    current_conditions: Dict[str, Any]
    historical_data: Optional[List[Dict[str, Any]]] = None


class YieldGapAnalysisRequest(BaseModel):
    actual_yield: float
    potential_yield: float
    crop_type: str
    farming_practices: Dict[str, Any]


class MarketTimingRequest(BaseModel):
    crop_type: str
    expected_harvest_date: str
    expected_quantity: float
    market_data: Dict[str, Any]


class PlantingScheduleRequest(BaseModel):
    crops: List[str]
    field_size: float
    climate_zone: str
    objectives: List[str]


class DailyBriefingRequest(BaseModel):
    farm_data: Dict[str, Any]


class AgentQueryRequest(BaseModel):
    query: str
    context: Dict[str, Any]


class ActionPlanRequest(BaseModel):
    goal: str
    timeframe: str
    farm_status: Dict[str, Any]
    constraints: Optional[List[str]] = None


class PerformanceAnalysisRequest(BaseModel):
    performance_data: Dict[str, Any]
    period: str


class EmergencyRequest(BaseModel):
    emergency_type: str
    details: Dict[str, Any]


# ===== CLIMATE MONITOR ROUTES =====

@router.post("/climate/analyze")
async def analyze_climate(request: ClimateAnalysisRequest):
    """Analyze climate conditions for a specific location."""
    try:
        result = await climate_agent.analyze_climate(
            location=request.location,
            climate_data=request.climate_data
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/climate/irrigation-recommendation")
async def get_irrigation_recommendation(request: IrrigationRecommendationRequest):
    """Get irrigation recommendations based on climate."""
    try:
        result = await climate_agent.get_irrigation_recommendation(
            climate_data=request.climate_data,
            crop_type=request.crop_type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/climate/weather-impact")
async def predict_weather_impact(request: WeatherImpactRequest):
    """Predict weather impact on crops."""
    try:
        result = await climate_agent.predict_weather_impact(
            forecast_data=request.forecast_data,
            crop_stage=request.crop_stage
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===== CROP ANALYZER ROUTES =====

@router.post("/crop/analyze-image")
async def analyze_crop_image(request: CropImageAnalysisRequest):
    """Analyze crop health from an image."""
    try:
        result = await crop_agent.analyze_crop_image(
            image_data=request.image_data,
            crop_type=request.crop_type,
            additional_info=request.additional_info
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crop/upload-image")
async def upload_crop_image(
    file: UploadFile = File(...),
    crop_type: str = "unknown"
):
    """Upload and analyze a crop image."""
    try:
        # Read image file
        contents = await file.read()
        
        # Convert to base64
        image_base64 = base64.b64encode(contents).decode('utf-8')
        
        # Analyze image
        result = await crop_agent.analyze_crop_image(
            image_data=image_base64,
            crop_type=crop_type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crop/identify-disease")
async def identify_disease(request: DiseaseIdentificationRequest):
    """Identify crop disease from symptoms."""
    try:
        result = await crop_agent.identify_disease(
            symptoms=request.symptoms,
            crop_type=request.crop_type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crop/nutrient-assessment")
async def assess_nutrient_deficiency(request: NutrientAssessmentRequest):
    """Assess nutrient deficiencies."""
    try:
        result = await crop_agent.assess_nutrient_deficiency(
            observations=request.observations,
            crop_type=request.crop_type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crop/rotation-recommendation")
async def recommend_crop_rotation(request: CropRotationRequest):
    """Recommend crop rotation strategy."""
    try:
        result = await crop_agent.recommend_crop_rotation(
            current_crop=request.current_crop,
            soil_condition=request.soil_condition,
            previous_crops=request.previous_crops
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===== WATER OPTIMIZER ROUTES =====

@router.post("/water/irrigation-schedule")
async def create_irrigation_schedule(request: IrrigationScheduleRequest):
    """Create an optimized irrigation schedule."""
    try:
        result = await water_agent.create_irrigation_schedule(
            crop_type=request.crop_type,
            field_size=request.field_size,
            soil_type=request.soil_type,
            climate_data=request.climate_data,
            water_availability=request.water_availability
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/water/efficiency")
async def calculate_water_efficiency(request: WaterEfficiencyRequest):
    """Calculate water usage efficiency."""
    try:
        result = await water_agent.calculate_water_efficiency(
            water_used=request.water_used,
            field_size=request.field_size,
            crop_yield=request.crop_yield,
            crop_type=request.crop_type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/water/detect-issues")
async def detect_irrigation_issues(request: IrrigationIssuesRequest):
    """Detect irrigation system issues."""
    try:
        result = await water_agent.detect_irrigation_issues(
            sensor_data=request.sensor_data,
            irrigation_system=request.irrigation_system
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/water/technology-recommendation")
async def recommend_irrigation_technology(request: IrrigationTechnologyRequest):
    """Recommend optimal irrigation technology."""
    try:
        result = await water_agent.recommend_irrigation_technology(
            farm_details=request.farm_details,
            budget=request.budget,
            water_source=request.water_source
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===== YIELD PREDICTOR ROUTES =====

@router.post("/yield/predict")
async def predict_yield(request: YieldPredictionRequest):
    """Predict crop yield."""
    try:
        result = await yield_agent.predict_yield(
            crop_type=request.crop_type,
            field_size=request.field_size,
            planting_date=request.planting_date,
            current_conditions=request.current_conditions,
            historical_data=request.historical_data
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/yield/gap-analysis")
async def analyze_yield_gaps(request: YieldGapAnalysisRequest):
    """Analyze yield gaps."""
    try:
        result = await yield_agent.analyze_yield_gaps(
            actual_yield=request.actual_yield,
            potential_yield=request.potential_yield,
            crop_type=request.crop_type,
            farming_practices=request.farming_practices
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/yield/market-timing")
async def forecast_market_timing(request: MarketTimingRequest):
    """Forecast optimal market timing."""
    try:
        result = await yield_agent.forecast_market_timing(
            crop_type=request.crop_type,
            expected_harvest_date=request.expected_harvest_date,
            expected_quantity=request.expected_quantity,
            market_data=request.market_data
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/yield/planting-schedule")
async def optimize_planting_schedule(request: PlantingScheduleRequest):
    """Optimize planting schedule."""
    try:
        result = await yield_agent.optimize_planting_schedule(
            crops=request.crops,
            field_size=request.field_size,
            climate_zone=request.climate_zone,
            objectives=request.objectives
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===== FARM MANAGER ROUTES =====

@router.post("/farm/daily-briefing")
async def get_daily_briefing(request: DailyBriefingRequest):
    """Get daily farm briefing."""
    try:
        result = await farm_manager.get_daily_briefing(
            farm_data=request.farm_data
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/farm/query")
async def coordinate_agents(request: AgentQueryRequest):
    """Query the farm management system."""
    try:
        result = await farm_manager.coordinate_agents(
            query=request.query,
            context=request.context
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/farm/action-plan")
async def create_action_plan(request: ActionPlanRequest):
    """Create a comprehensive action plan."""
    try:
        result = await farm_manager.create_action_plan(
            goal=request.goal,
            timeframe=request.timeframe,
            farm_status=request.farm_status,
            constraints=request.constraints
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/farm/performance")
async def analyze_farm_performance(request: PerformanceAnalysisRequest):
    """Analyze farm performance."""
    try:
        result = await farm_manager.analyze_farm_performance(
            performance_data=request.performance_data,
            period=request.period
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/farm/emergency")
async def handle_emergency(request: EmergencyRequest):
    """Handle farm emergency."""
    try:
        result = await farm_manager.handle_emergency(
            emergency_type=request.emergency_type,
            details=request.details
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/agents")
async def list_agents():
    """List all available agents and their capabilities."""
    return {
        "agents": [
            {
                "name": "climate_monitor",
                "description": "Monitors weather and climate conditions",
                "endpoints": [
                    "/climate/analyze",
                    "/climate/irrigation-recommendation",
                    "/climate/weather-impact"
                ]
            },
            {
                "name": "crop_analyzer",
                "description": "Analyzes crop health and diseases",
                "endpoints": [
                    "/crop/analyze-image",
                    "/crop/upload-image",
                    "/crop/identify-disease",
                    "/crop/nutrient-assessment",
                    "/crop/rotation-recommendation"
                ]
            },
            {
                "name": "water_optimizer",
                "description": "Optimizes water usage and irrigation",
                "endpoints": [
                    "/water/irrigation-schedule",
                    "/water/efficiency",
                    "/water/detect-issues",
                    "/water/technology-recommendation"
                ]
            },
            {
                "name": "yield_predictor",
                "description": "Predicts yields and optimizes production",
                "endpoints": [
                    "/yield/predict",
                    "/yield/gap-analysis",
                    "/yield/market-timing",
                    "/yield/planting-schedule"
                ]
            },
            {
                "name": "farm_manager",
                "description": "Coordinates all agents for comprehensive farm management",
                "endpoints": [
                    "/farm/daily-briefing",
                    "/farm/query",
                    "/farm/action-plan",
                    "/farm/performance",
                    "/farm/emergency"
                ]
            }
        ]
    }

