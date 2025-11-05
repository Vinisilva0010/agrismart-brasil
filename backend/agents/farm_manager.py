"""
Farm Manager Agent
Orchestrates all agents and provides comprehensive farm management insights.
"""

import os
from typing import Dict, Any, List
from google import genai
from google.genai import types
from .climate_monitor import ClimateMonitorAgent
from .crop_analyzer import CropAnalyzerAgent
from .water_optimizer import WaterOptimizerAgent
from .yield_predictor import YieldPredictorAgent


class FarmManagerAgent:
    """Master agent that coordinates all other agents for comprehensive farm management."""
    
    def __init__(self):
        """Initialize the Farm Manager Agent and all sub-agents."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.0-flash-exp"
        
        # Initialize all specialized agents
        self.climate_agent = ClimateMonitorAgent()
        self.crop_agent = CropAnalyzerAgent()
        self.water_agent = WaterOptimizerAgent()
        self.yield_agent = YieldPredictorAgent()
    
    async def get_daily_briefing(self, farm_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a comprehensive daily farm briefing.
        
        Args:
            farm_data: Current farm status and data
            
        Returns:
            Daily briefing with insights from all agents
        """
        try:
            prompt = f"""
            Generate a comprehensive daily farm management briefing:
            
            Farm Overview:
            - Location: {farm_data.get('location', 'N/A')}
            - Total Area: {farm_data.get('total_area', 'N/A')} hectares
            - Active Crops: {farm_data.get('active_crops', 'N/A')}
            - Current Season: {farm_data.get('season', 'N/A')}
            
            Weather:
            - Temperature: {farm_data.get('temperature', 'N/A')}°C
            - Conditions: {farm_data.get('weather_conditions', 'N/A')}
            - Forecast: {farm_data.get('forecast', 'N/A')}
            
            Current Status:
            - Pending Tasks: {farm_data.get('pending_tasks', 'N/A')}
            - Alerts: {farm_data.get('alerts', 'N/A')}
            
            Forneça um briefing diário estruturado em português com:
            
            📋 PRIORIDADES DE HOJE:
            - Liste as ações mais importantes
            
            🌤️ CLIMA E IMPACTOS:
            - Condições do tempo e como afetam as operações
            
            🌱 SAÚDE DAS CULTURAS:
            - Status geral das plantações
            
            💧 IRRIGAÇÃO:
            - Necessidades de água hoje
            
            ⚠️ ALERTAS E RISCOS:
            - Questões que precisam de atenção
            
            ✅ OPORTUNIDADES:
            - Ações recomendadas para otimizar resultados
            
            Use linguagem clara e objetiva.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "farm_manager",
                "briefing_date": farm_data.get('date', 'today'),
                "briefing": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "farm_manager",
                "error": str(e)
            }
    
    async def coordinate_agents(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Coordinate multiple agents to answer complex queries.
        
        Args:
            query: User's query or request
            context: Contextual information about the farm
            
        Returns:
            Coordinated response from relevant agents
        """
        try:
            # Determine which agents are needed
            routing_prompt = f"""
            Analyze this farm management query and determine which specialized agents should handle it:
            
            Query: {query}
            Context: {context}
            
            Available agents:
            - climate_monitor: Weather, climate analysis, irrigation timing
            - crop_analyzer: Crop health, diseases, nutrient analysis
            - water_optimizer: Irrigation scheduling, water efficiency
            - yield_predictor: Yield forecasting, market timing, planting schedules
            
            Respond with JSON array of agents to consult: ["agent1", "agent2", ...]
            """
            
            routing_response = self.client.models.generate_content(
                model=self.model_id,
                contents=routing_prompt
            )
            
            # For now, provide a comprehensive response
            comprehensive_prompt = f"""
            As a comprehensive farm management AI, answer this query:
            
            Query: {query}
            
            Farm Context:
            {context}
            
            Provide a detailed, actionable response in clear Portuguese covering:
            - Resposta direta à pergunta
            - Dados e raciocínio de suporte
            - Recomendações passo a passo
            - Riscos potenciais e considerações
            - Resultados esperados
            
            Use formatação clara com marcadores e parágrafos curtos.
            Seja objetivo e prático.
            """
            
            final_response = self.client.models.generate_content(
                model=self.model_id,
                contents=comprehensive_prompt
            )
            
            return {
                "status": "success",
                "agent": "farm_manager",
                "query": query,
                "response": final_response.text,
                "routing": routing_response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "farm_manager",
                "error": str(e)
            }
    
    async def create_action_plan(
        self,
        goal: str,
        timeframe: str,
        farm_status: Dict[str, Any],
        constraints: List[str] = None
    ) -> Dict[str, Any]:
        """
        Create a comprehensive action plan to achieve a farming goal.
        
        Args:
            goal: Farming goal to achieve
            timeframe: Time period for the goal
            farm_status: Current farm status
            constraints: Budget, resource, or other constraints
            
        Returns:
            Detailed action plan with timeline and resources
        """
        try:
            constraints_str = ', '.join(constraints) if constraints else 'None specified'
            
            prompt = f"""
            Create a comprehensive action plan for this farming goal:
            
            Goal: {goal}
            Timeframe: {timeframe}
            
            Current Farm Status:
            {farm_status}
            
            Constraints: {constraints_str}
            
            Provide a detailed action plan including:
            1. Milestones and phases
            2. Week-by-week or month-by-month tasks
            3. Resource requirements (labor, equipment, inputs)
            4. Budget estimates
            5. Success metrics and KPIs
            6. Risk mitigation strategies
            7. Contingency plans
            8. Expected outcomes and ROI
            
            Format as JSON with timeline, tasks, resources, and metrics.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "farm_manager",
                "goal": goal,
                "action_plan": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "farm_manager",
                "error": str(e)
            }
    
    async def analyze_farm_performance(
        self,
        performance_data: Dict[str, Any],
        period: str
    ) -> Dict[str, Any]:
        """
        Analyze overall farm performance and provide insights.
        
        Args:
            performance_data: Farm performance metrics
            period: Time period for analysis
            
        Returns:
            Performance analysis with insights and recommendations
        """
        try:
            prompt = f"""
            Analyze farm performance for {period}:
            
            Performance Metrics:
            - Total Yield: {performance_data.get('total_yield', 'N/A')} tons
            - Revenue: ${performance_data.get('revenue', 'N/A')}
            - Costs: ${performance_data.get('costs', 'N/A')}
            - Profit Margin: {performance_data.get('profit_margin', 'N/A')}%
            - Water Usage: {performance_data.get('water_usage', 'N/A')} m³
            - Crop Health Incidents: {performance_data.get('health_incidents', 'N/A')}
            - Yield per Hectare: {performance_data.get('yield_per_ha', 'N/A')} tons
            
            Benchmarks:
            {performance_data.get('benchmarks', 'N/A')}
            
            Provide comprehensive analysis:
            1. Overall performance rating
            2. Strengths and successes
            3. Areas for improvement
            4. Comparison with benchmarks and previous periods
            5. Key insights and patterns
            6. Strategic recommendations for next period
            7. Efficiency opportunities
            8. Investment priorities
            
            Format as JSON with detailed analysis and action items.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "farm_manager",
                "period": period,
                "analysis": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "farm_manager",
                "error": str(e)
            }
    
    async def handle_emergency(self, emergency_type: str, details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle farm emergencies with immediate action recommendations.
        
        Args:
            emergency_type: Type of emergency (pest outbreak, frost, drought, etc.)
            details: Emergency details
            
        Returns:
            Emergency response plan
        """
        try:
            prompt = f"""
            EMERGENCY RESPONSE REQUIRED
            
            Emergency Type: {emergency_type}
            Details: {details}
            
            Provide immediate emergency response plan:
            1. IMMEDIATE ACTIONS (next 1-4 hours)
            2. SHORT-TERM ACTIONS (next 24-48 hours)
            3. Resources needed urgently
            4. Expected damage/impact assessment
            5. Prevention of further damage
            6. Recovery plan
            7. Long-term mitigation strategies
            8. Contacts/resources to mobilize
            
            Format as JSON with URGENT actions clearly marked.
            Prioritize crop and livestock safety.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "farm_manager",
                "emergency_type": emergency_type,
                "priority": "URGENT",
                "response_plan": response.text
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "farm_manager",
                "error": str(e)
            }

