"""
Water Optimizer Agent
Optimizes water usage and irrigation schedules for sustainable agriculture.
"""

import os
from typing import Dict, Any, List
from datetime import datetime, timedelta
from google import genai
from google.genai import types


class WaterOptimizerAgent:
    """Agent responsible for optimizing water usage and irrigation."""
    
    def __init__(self):
        """Initialize the Water Optimizer Agent with Gemini 2.0 Flash."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.0-flash-exp"
    
    async def create_irrigation_schedule(
        self, 
        crop_type: str, 
        field_size: float,
        soil_type: str,
        climate_data: Dict[str, Any],
        water_availability: str
    ) -> Dict[str, Any]:
        """
        Create an optimized irrigation schedule.
        
        Args:
            crop_type: Type of crop
            field_size: Field size in hectares
            soil_type: Type of soil (sandy, loamy, clay, etc.)
            climate_data: Current and forecasted climate data
            water_availability: Available water resources status
            
        Returns:
            Detailed irrigation schedule with water optimization
        """
        try:
            prompt = f"""
            Create an optimal irrigation schedule for the next 14 days:
            
            Crop Type: {crop_type}
            Field Size: {field_size} hectares
            Soil Type: {soil_type}
            Current Temperature: {climate_data.get('temperature', 'N/A')}°C
            Humidity: {climate_data.get('humidity', 'N/A')}%
            Rainfall Forecast: {climate_data.get('rainfall_forecast', 'N/A')}
            Water Availability: {water_availability}
            
            Provide a detailed 14-day irrigation schedule including:
            1. Daily irrigation requirements (yes/no, volume in liters)
            2. Best time for irrigation each day
            3. Expected water consumption total
            4. Water-saving opportunities
            5. Efficiency optimization tips
            6. Contingency plans for water shortage
            
            Format as JSON with a daily schedule array and summary statistics.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "water_optimizer",
                "crop_type": crop_type,
                "field_size": field_size,
                "schedule": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "water_optimizer",
                "error": str(e)
            }
    
    async def calculate_water_efficiency(
        self,
        water_used: float,
        field_size: float,
        crop_yield: float,
        crop_type: str
    ) -> Dict[str, Any]:
        """
        Calculate water usage efficiency metrics.
        
        Args:
            water_used: Total water used in cubic meters
            field_size: Field size in hectares
            crop_yield: Actual crop yield in tons
            crop_type: Type of crop
            
        Returns:
            Water efficiency metrics and improvement suggestions
        """
        try:
            prompt = f"""
            Calculate and analyze water usage efficiency:
            
            Crop: {crop_type}
            Water Used: {water_used} m³
            Field Size: {field_size} hectares
            Crop Yield: {crop_yield} tons
            
            Provide:
            1. Water productivity (kg per m³)
            2. Comparison with industry benchmarks for {crop_type}
            3. Efficiency rating (poor, fair, good, excellent)
            4. Specific recommendations to improve water efficiency
            5. Potential water savings (percentage and volume)
            6. ROI of implementing water-saving technologies
            
            Format as JSON with detailed metrics and actionable recommendations.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "water_optimizer",
                "metrics": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "water_optimizer",
                "error": str(e)
            }
    
    async def detect_irrigation_issues(
        self,
        sensor_data: Dict[str, Any],
        irrigation_system: str
    ) -> Dict[str, Any]:
        """
        Detect potential irrigation system issues.
        
        Args:
            sensor_data: Data from soil moisture and irrigation sensors
            irrigation_system: Type of irrigation system (drip, sprinkler, etc.)
            
        Returns:
            Issue detection and maintenance recommendations
        """
        try:
            prompt = f"""
            Analyze irrigation system performance and detect issues:
            
            System Type: {irrigation_system}
            Sensor Data:
            - Soil Moisture Zones: {sensor_data.get('moisture_zones', 'N/A')}
            - Water Pressure: {sensor_data.get('water_pressure', 'N/A')} bar
            - Flow Rate: {sensor_data.get('flow_rate', 'N/A')} L/min
            - Coverage Uniformity: {sensor_data.get('coverage_uniformity', 'N/A')}%
            
            Identify:
            1. Potential system issues (leaks, clogs, pressure problems)
            2. Uneven water distribution areas
            3. Maintenance requirements
            4. System efficiency rating
            5. Repair/upgrade recommendations
            6. Preventive maintenance schedule
            
            Format as JSON with issues array and recommendations.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "water_optimizer",
                "system_type": irrigation_system,
                "analysis": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "water_optimizer",
                "error": str(e)
            }
    
    async def recommend_irrigation_technology(
        self,
        farm_details: Dict[str, Any],
        budget: str,
        water_source: str
    ) -> Dict[str, Any]:
        """
        Recommend optimal irrigation technology.
        
        Args:
            farm_details: Farm size, crops, terrain, etc.
            budget: Available budget range
            water_source: Primary water source
            
        Returns:
            Technology recommendations with cost-benefit analysis
        """
        try:
            prompt = f"""
            Recommend the best irrigation technology for this farm:
            
            Farm Size: {farm_details.get('size', 'N/A')} hectares
            Crops: {farm_details.get('crops', 'N/A')}
            Terrain: {farm_details.get('terrain', 'N/A')}
            Current System: {farm_details.get('current_system', 'None')}
            Budget: {budget}
            Water Source: {water_source}
            
            Provide:
            1. Top 3 recommended irrigation technologies
            2. Cost estimates for each option
            3. Water savings potential (%)
            4. Installation complexity and timeline
            5. Maintenance requirements
            6. Expected ROI and payback period
            7. Environmental benefits
            
            Format as JSON with detailed comparison and final recommendation.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "water_optimizer",
                "recommendations": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "water_optimizer",
                "error": str(e)
            }

