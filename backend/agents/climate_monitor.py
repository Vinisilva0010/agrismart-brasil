"""
Climate Monitor Agent
Monitors weather conditions and provides climate-related insights for agriculture.
"""

import os
from typing import Dict, Any
from google import genai
from google.genai import types


class ClimateMonitorAgent:
    """Agent responsible for monitoring climate and weather conditions."""
    
    def __init__(self):
        """Initialize the Climate Monitor Agent with Gemini 2.0 Flash."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.0-flash-exp"
        
    async def analyze_climate(self, location: str, climate_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze climate conditions for a specific location.
        
        Args:
            location: Farm location
            climate_data: Current climate data (temperature, humidity, rainfall, etc.)
            
        Returns:
            Analysis results with recommendations
        """
        try:
            prompt = f"""
            You are an expert agricultural climate analyst. Analyze the following climate data for a farm in {location}:
            
            Temperature: {climate_data.get('temperature', 'N/A')}°C
            Humidity: {climate_data.get('humidity', 'N/A')}%
            Rainfall: {climate_data.get('rainfall', 'N/A')}mm
            Wind Speed: {climate_data.get('wind_speed', 'N/A')} km/h
            UV Index: {climate_data.get('uv_index', 'N/A')}
            
            Provide:
            1. Current climate conditions assessment
            2. Risk factors for crops
            3. Immediate action recommendations
            4. 7-day outlook and planning suggestions
            
            Format your response as a structured JSON with keys: assessment, risks, recommendations, outlook.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "climate_monitor",
                "location": location,
                "analysis": response.text,
                "data": climate_data
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "climate_monitor",
                "error": str(e)
            }
    
    async def get_irrigation_recommendation(self, climate_data: Dict[str, Any], crop_type: str) -> Dict[str, Any]:
        """
        Get irrigation recommendations based on climate conditions.
        
        Args:
            climate_data: Current climate data
            crop_type: Type of crop being grown
            
        Returns:
            Irrigation recommendations
        """
        try:
            prompt = f"""
            As an agricultural climate expert, recommend irrigation strategy for {crop_type} based on:
            
            Temperature: {climate_data.get('temperature', 'N/A')}°C
            Humidity: {climate_data.get('humidity', 'N/A')}%
            Recent Rainfall: {climate_data.get('rainfall', 'N/A')}mm
            Soil Moisture: {climate_data.get('soil_moisture', 'N/A')}%
            
            Provide specific irrigation recommendations including:
            - Whether to irrigate today (yes/no)
            - Recommended water amount (liters per hectare)
            - Best time of day for irrigation
            - Expected duration
            
            Respond in JSON format with keys: should_irrigate, water_amount, best_time, duration, reasoning.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "climate_monitor",
                "crop_type": crop_type,
                "recommendation": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "climate_monitor",
                "error": str(e)
            }
    
    async def predict_weather_impact(self, forecast_data: Dict[str, Any], crop_stage: str) -> Dict[str, Any]:
        """
        Predict weather impact on crops.
        
        Args:
            forecast_data: Weather forecast data
            crop_stage: Current growth stage of the crop
            
        Returns:
            Impact prediction and recommendations
        """
        try:
            prompt = f"""
            Analyze the weather forecast impact on crops at {crop_stage} stage:
            
            Forecast: {forecast_data}
            
            Provide:
            1. Potential positive impacts
            2. Potential negative impacts
            3. Preventive measures
            4. Opportunity recommendations
            
            Respond in JSON format.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "climate_monitor",
                "prediction": response.text,
                "crop_stage": crop_stage
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "climate_monitor",
                "error": str(e)
            }

