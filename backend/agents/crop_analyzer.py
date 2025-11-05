"""
Crop Analyzer Agent
Analyzes crop health through images and provides diagnostic insights.
"""

import os
import base64
from typing import Dict, Any, Optional
from google import genai
from google.genai import types


class CropAnalyzerAgent:
    """Agent responsible for analyzing crop health and diseases."""
    
    def __init__(self):
        """Initialize the Crop Analyzer Agent with Gemini 2.0 Flash."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.0-flash-exp"
    
    async def analyze_crop_image(self, image_data: str, crop_type: str, additional_info: Optional[str] = None) -> Dict[str, Any]:
        """
        Analyze crop health from an image.
        
        Args:
            image_data: Base64 encoded image or image URL
            crop_type: Type of crop in the image
            additional_info: Additional context about the crop
            
        Returns:
            Analysis results with health assessment and recommendations
        """
        try:
            prompt = f"""
            You are an expert agricultural crop health analyst. Analyze this image of {crop_type}.
            
            Additional context: {additional_info or 'None provided'}
            
            Provide a detailed analysis including:
            1. Overall health status (healthy, stressed, diseased, etc.)
            2. Identified issues (diseases, pests, nutrient deficiencies, etc.)
            3. Severity level (low, medium, high, critical)
            4. Specific recommendations for treatment or intervention
            5. Preventive measures for future
            6. Confidence level of the diagnosis
            
            Format your response as JSON with keys: health_status, issues, severity, recommendations, prevention, confidence.
            """
            
            # Handle both base64 and URL formats
            if image_data.startswith('http'):
                contents = [
                    types.Part.from_uri(file_uri=image_data, mime_type="image/jpeg"),
                    types.Part.from_text(prompt)
                ]
            else:
                contents = [
                    types.Part.from_bytes(data=base64.b64decode(image_data), mime_type="image/jpeg"),
                    types.Part.from_text(prompt)
                ]
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=contents
            )
            
            return {
                "status": "success",
                "agent": "crop_analyzer",
                "crop_type": crop_type,
                "analysis": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "crop_analyzer",
                "error": str(e)
            }
    
    async def identify_disease(self, symptoms: str, crop_type: str) -> Dict[str, Any]:
        """
        Identify potential crop disease from described symptoms.
        
        Args:
            symptoms: Description of observed symptoms
            crop_type: Type of crop affected
            
        Returns:
            Disease identification and treatment recommendations
        """
        try:
            prompt = f"""
            As a crop disease expert, identify the disease affecting {crop_type} with these symptoms:
            
            {symptoms}
            
            Provide:
            1. Most likely disease(s) - list top 3 possibilities with probability
            2. Detailed description of each disease
            3. Treatment options (organic and chemical)
            4. Expected recovery timeline
            5. Risk of spread to other crops
            6. Prevention strategies
            
            Format as JSON with keys: diseases (array), treatments, recovery_time, spread_risk, prevention.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "crop_analyzer",
                "crop_type": crop_type,
                "diagnosis": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "crop_analyzer",
                "error": str(e)
            }
    
    async def assess_nutrient_deficiency(self, observations: Dict[str, Any], crop_type: str) -> Dict[str, Any]:
        """
        Assess nutrient deficiencies based on visual observations.
        
        Args:
            observations: Visual observations (leaf color, growth patterns, etc.)
            crop_type: Type of crop
            
        Returns:
            Nutrient deficiency assessment and fertilization recommendations
        """
        try:
            prompt = f"""
            Analyze these observations for {crop_type} to identify nutrient deficiencies:
            
            Leaf Color: {observations.get('leaf_color', 'N/A')}
            Leaf Patterns: {observations.get('leaf_patterns', 'N/A')}
            Growth Rate: {observations.get('growth_rate', 'N/A')}
            Stem Condition: {observations.get('stem_condition', 'N/A')}
            Other Notes: {observations.get('notes', 'N/A')}
            
            Provide:
            1. Identified nutrient deficiencies (N, P, K, micronutrients)
            2. Confidence level for each deficiency
            3. Recommended fertilizer type and amount
            4. Application method and timing
            5. Expected improvement timeline
            
            Format as JSON.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "crop_analyzer",
                "crop_type": crop_type,
                "assessment": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "crop_analyzer",
                "error": str(e)
            }
    
    async def recommend_crop_rotation(self, current_crop: str, soil_condition: str, previous_crops: list) -> Dict[str, Any]:
        """
        Recommend crop rotation strategy.
        
        Args:
            current_crop: Currently planted crop
            soil_condition: Current soil condition
            previous_crops: List of previously grown crops
            
        Returns:
            Crop rotation recommendations
        """
        try:
            prompt = f"""
            Recommend an optimal crop rotation strategy:
            
            Current Crop: {current_crop}
            Soil Condition: {soil_condition}
            Previous Crops (last 3 seasons): {', '.join(previous_crops)}
            
            Provide:
            1. Recommended next crop(s) - top 3 options
            2. Reasoning for each recommendation
            3. Expected soil health improvements
            4. Pest and disease management benefits
            5. Economic considerations
            6. Timeline and seasonal considerations
            
            Format as JSON with detailed explanations.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "crop_analyzer",
                "recommendations": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "crop_analyzer",
                "error": str(e)
            }

