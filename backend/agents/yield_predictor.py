"""
Yield Predictor Agent
Predicts crop yields and provides production forecasts.
"""

import os
from typing import Dict, Any, List
from datetime import datetime
from google import genai
from google.genai import types


class YieldPredictorAgent:
    """Agent responsible for predicting crop yields and production forecasts."""
    
    def __init__(self):
        """Initialize the Yield Predictor Agent with Gemini 2.0 Flash."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.0-flash-exp"
    
    async def predict_yield(
        self,
        crop_type: str,
        field_size: float,
        planting_date: str,
        current_conditions: Dict[str, Any],
        historical_data: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Predict crop yield based on various factors.
        
        Args:
            crop_type: Type of crop
            field_size: Field size in hectares
            planting_date: Date when crop was planted
            current_conditions: Current growing conditions
            historical_data: Historical yield data from previous seasons
            
        Returns:
            Yield prediction with confidence intervals
        """
        try:
            historical_summary = "No historical data provided"
            if historical_data:
                historical_summary = "\n".join([
                    f"Year {data.get('year', 'N/A')}: {data.get('yield', 'N/A')} tons/ha"
                    for data in historical_data
                ])
            
            prompt = f"""
            Predict the expected crop yield for this season:
            
            Crop Type: {crop_type}
            Field Size: {field_size} hectares
            Planting Date: {planting_date}
            
            Current Conditions:
            - Growth Stage: {current_conditions.get('growth_stage', 'N/A')}
            - Health Status: {current_conditions.get('health_status', 'N/A')}
            - Soil Quality: {current_conditions.get('soil_quality', 'N/A')}
            - Weather Conditions: {current_conditions.get('weather', 'N/A')}
            - Irrigation: {current_conditions.get('irrigation', 'N/A')}
            - Fertilization: {current_conditions.get('fertilization', 'N/A')}
            
            Historical Yields:
            {historical_summary}
            
            Provide:
            1. Expected yield (tons per hectare and total)
            2. Confidence level (low, medium, high)
            3. Yield range (minimum, expected, maximum)
            4. Key factors influencing the prediction
            5. Risks that could reduce yield
            6. Opportunities to increase yield
            7. Expected harvest date
            
            Format as JSON with detailed predictions and analysis.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "yield_predictor",
                "crop_type": crop_type,
                "prediction": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "yield_predictor",
                "error": str(e)
            }
    
    async def analyze_yield_gaps(
        self,
        actual_yield: float,
        potential_yield: float,
        crop_type: str,
        farming_practices: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Analyze the gap between actual and potential yield.
        
        Args:
            actual_yield: Actual yield achieved (tons/ha)
            potential_yield: Potential/benchmark yield (tons/ha)
            crop_type: Type of crop
            farming_practices: Current farming practices
            
        Returns:
            Yield gap analysis with improvement recommendations
        """
        try:
            prompt = f"""
            Analyze the yield gap and provide improvement strategies:
            
            Crop: {crop_type}
            Actual Yield: {actual_yield} tons/ha
            Potential Yield: {potential_yield} tons/ha
            Yield Gap: {potential_yield - actual_yield} tons/ha ({((potential_yield - actual_yield) / potential_yield * 100):.1f}%)
            
            Current Practices:
            - Seed Variety: {farming_practices.get('seed_variety', 'N/A')}
            - Planting Method: {farming_practices.get('planting_method', 'N/A')}
            - Fertilization: {farming_practices.get('fertilization', 'N/A')}
            - Irrigation: {farming_practices.get('irrigation', 'N/A')}
            - Pest Control: {farming_practices.get('pest_control', 'N/A')}
            - Harvest Method: {farming_practices.get('harvest_method', 'N/A')}
            
            Provide:
            1. Main causes of the yield gap
            2. Prioritized recommendations to close the gap
            3. Expected yield improvement from each recommendation
            4. Cost-benefit analysis for each improvement
            5. Implementation timeline and steps
            6. Realistic yield target for next season
            
            Format as JSON with actionable recommendations.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "yield_predictor",
                "analysis": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "yield_predictor",
                "error": str(e)
            }
    
    async def forecast_market_timing(
        self,
        crop_type: str,
        expected_harvest_date: str,
        expected_quantity: float,
        market_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Forecast optimal market timing for selling crops.
        
        Args:
            crop_type: Type of crop
            expected_harvest_date: Expected harvest date
            expected_quantity: Expected quantity to sell (tons)
            market_data: Current market prices and trends
            
        Returns:
            Market timing recommendations
        """
        try:
            prompt = f"""
            Provide market timing recommendations for crop sales:
            
            Crop: {crop_type}
            Expected Harvest: {expected_harvest_date}
            Expected Quantity: {expected_quantity} tons
            
            Market Data:
            - Current Price: {market_data.get('current_price', 'N/A')} per ton
            - Price Trend: {market_data.get('price_trend', 'N/A')}
            - Demand Forecast: {market_data.get('demand_forecast', 'N/A')}
            - Storage Costs: {market_data.get('storage_cost', 'N/A')} per ton/month
            
            Provide:
            1. Optimal selling strategy (immediate sale vs. storage)
            2. Expected price movements (next 3-6 months)
            3. Revenue optimization recommendations
            4. Risk assessment (price volatility, storage risks)
            5. Recommended portion to sell immediately vs. store
            6. Expected ROI for different strategies
            
            Format as JSON with detailed financial projections.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "yield_predictor",
                "forecast": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "yield_predictor",
                "error": str(e)
            }
    
    async def optimize_planting_schedule(
        self,
        crops: List[str],
        field_size: float,
        climate_zone: str,
        objectives: List[str]
    ) -> Dict[str, Any]:
        """
        Optimize planting schedule for multiple crops.
        
        Args:
            crops: List of crops to plan for
            field_size: Total available field size
            climate_zone: Climate zone information
            objectives: Farming objectives (max yield, cash flow, etc.)
            
        Returns:
            Optimized planting schedule
        """
        try:
            prompt = f"""
            Create an optimized planting schedule for maximum productivity:
            
            Crops to Plan: {', '.join(crops)}
            Total Field Size: {field_size} hectares
            Climate Zone: {climate_zone}
            Objectives: {', '.join(objectives)}
            
            Provide:
            1. Recommended planting calendar (month-by-month)
            2. Field allocation for each crop
            3. Crop rotation strategy
            4. Expected total annual yield
            5. Expected revenue projection
            6. Resource requirements (water, labor, inputs)
            7. Risk mitigation through diversification
            
            Format as JSON with detailed monthly schedule and financial projections.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "yield_predictor",
                "schedule": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "yield_predictor",
                "error": str(e)
            }

