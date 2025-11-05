"""
Farm Manager Agent - IMPLEMENTAÇÃO COM GOOGLE ADK
Orquestra todos os agentes usando Google Agent Development Kit.
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
    """
    Agente Gerente da Fazenda - Coordena todos os agentes especializados.
    Usa Google ADK para orquestração multi-agente.
    """
    
    def __init__(self):
        """Initialize the Farm Manager Agent with Google ADK."""
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
        
        # System instruction em português para o Farm Manager
        self.system_instruction = """
        Você é o AgriSmart Brasil AI - um assistente especializado em gestão agrícola brasileira.
        
        ESPECIALIDADES:
        - Agricultura brasileira (soja, milho, café, cana-de-açúcar)
        - Clima e meteorologia do Brasil (cerrado, pampa, pantanal)
        - Gestão de fazendas e propriedades rurais
        - Irrigação e recursos hídricos
        - Previsão de safras e produtividade
        
        CONTEXTO BRASILEIRO:
        - Safra e entressafra no Brasil
        - Épocas de plantio e colheita regionais
        - Pragas e doenças comuns no Brasil
        - Regulamentações brasileiras (MAPA, ANVISA)
        - Mercado agrícola brasileiro
        
        COORDENAÇÃO DE AGENTES:
        Você coordena 4 agentes especializados:
        1. Monitor Climático - análise do tempo e clima
        2. Analisador de Culturas - saúde das plantas, pragas, doenças
        3. Otimizador de Água - irrigação eficiente
        4. Preditor de Produção - previsão de safras
        
        INSTRUÇÕES:
        - Responda SEMPRE em português brasileiro claro e objetivo
        - Use dados científicos e técnicos quando apropriado
        - Seja prático e acionável nas recomendações
        - Considere as condições específicas do Brasil
        - Forneça explicações completas mas concisas
        - Use marcadores e formatação para clareza
        
        FORMATO DE RESPOSTA:
        - Use emojis para tornar as respostas mais visuais (🌾 🌤️ 💧 📊)
        - Organize informações com títulos e seções
        - Liste ações prioritárias quando relevante
        - Inclua alertas importantes no início
        """
    
    async def chat(self, user_message: str, farm_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Chat principal com o usuário usando coordenação multi-agente.
        
        Args:
            user_message: Mensagem do usuário
            farm_context: Contexto da fazenda (localização, culturas, etc.)
            
        Returns:
            Resposta coordenada dos agentes
        """
        try:
            # Preparar contexto
            context_str = ""
            if farm_context:
                context_str = f"""
                CONTEXTO DA FAZENDA:
                - Localização: {farm_context.get('location', 'Brasil')}
                - Culturas: {', '.join(farm_context.get('crops', ['Soja', 'Milho']))}
                - Área: {farm_context.get('size', 'N/A')} hectares
                - Estação: {farm_context.get('season', 'Safra 2024/2025')}
                """
            
            # Combinar instrução do sistema com contexto e mensagem
            full_prompt = f"""
            {self.system_instruction}
            
            {context_str}
            
            MENSAGEM DO USUÁRIO:
            {user_message}
            
            Forneça uma resposta completa e útil em português brasileiro.
            Se necessário, considere informações dos agentes especializados disponíveis.
            """
            
            # Gerar resposta usando Gemini 2.0 Flash
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    top_p=0.95,
                    max_output_tokens=2048,
                )
            )
            
            return {
                "status": "success",
                "agent": "farm_manager",
                "response": response.text,
                "context_used": farm_context is not None
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "farm_manager",
                "error": str(e)
            }
    
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
            Gere um briefing diário completo para gestão da fazenda.
            
            DADOS DA FAZENDA:
            - Localização: {farm_data.get('location', 'N/A')}
            - Área Total: {farm_data.get('total_area', 'N/A')} hectares
            - Culturas Ativas: {', '.join(farm_data.get('active_crops', []))}
            - Estação: {farm_data.get('season', 'N/A')}
            
            CLIMA ATUAL:
            - Temperatura: {farm_data.get('temperature', 'N/A')}°C
            - Condições: {farm_data.get('weather_conditions', 'N/A')}
            - Previsão: {farm_data.get('forecast', 'N/A')}
            
            STATUS ATUAL:
            - Tarefas Pendentes: {farm_data.get('pending_tasks', 'N/A')}
            - Alertas: {farm_data.get('alerts', 'N/A')}
            
            Forneça um briefing estruturado em português com:
            
            📋 PRIORIDADES DE HOJE:
            - Liste as ações mais importantes para hoje
            
            🌤️ CLIMA E IMPACTOS:
            - Condições do tempo e como afetam as operações
            
            🌱 SAÚDE DAS CULTURAS:
            - Status geral das plantações
            
            💧 IRRIGAÇÃO:
            - Necessidades de água para hoje
            
            ⚠️ ALERTAS E RISCOS:
            - Questões que precisam de atenção imediata
            
            ✅ OPORTUNIDADES:
            - Ações recomendadas para otimizar resultados
            
            Use linguagem clara, objetiva e acionável.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.7)
            )
            
            return {
                "status": "success",
                "agent": "farm_manager",
                "briefing_date": farm_data.get('date', 'hoje'),
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
        Coordena múltiplos agentes para responder queries complexas.
        
        Args:
            query: Pergunta ou solicitação do usuário
            context: Contexto da fazenda
            
        Returns:
            Resposta coordenada
        """
        # Usar o método chat que já tem a lógica de coordenação
        return await self.chat(query, context)
    
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
            constraints_str = ', '.join(constraints) if constraints else 'Nenhuma especificada'
            
            prompt = f"""
            Crie um plano de ação detalhado para alcançar este objetivo agrícola:
            
            OBJETIVO: {goal}
            PRAZO: {timeframe}
            
            STATUS ATUAL DA FAZENDA:
            {farm_status}
            
            RESTRIÇÕES: {constraints_str}
            
            Forneça um plano de ação abrangente em português incluindo:
            
            🎯 VISÃO GERAL DO PLANO:
            - Objetivo principal e metas intermediárias
            
            📅 CRONOGRAMA:
            - Fases do projeto (semana a semana ou mês a mês)
            - Marcos principais e entregas
            
            🔧 RECURSOS NECESSÁRIOS:
            - Mão de obra
            - Equipamentos
            - Insumos agrícolas
            - Estimativa de custos
            
            📊 MÉTRICAS DE SUCESSO:
            - KPIs para acompanhamento
            - Como medir o progresso
            
            ⚠️ GESTÃO DE RISCOS:
            - Riscos identificados
            - Estratégias de mitigação
            - Planos de contingência
            
            ✅ RESULTADOS ESPERADOS:
            - Impactos esperados
            - ROI estimado
            
            Seja específico, prático e considere as condições brasileiras.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.7)
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
            Analise o desempenho da fazenda para o período: {period}
            
            MÉTRICAS DE DESEMPENHO:
            - Produção Total: {performance_data.get('total_yield', 'N/A')} toneladas
            - Receita: R$ {performance_data.get('revenue', 'N/A')}
            - Custos: R$ {performance_data.get('costs', 'N/A')}
            - Margem de Lucro: {performance_data.get('profit_margin', 'N/A')}%
            - Uso de Água: {performance_data.get('water_usage', 'N/A')} m³
            - Incidentes de Saúde das Culturas: {performance_data.get('health_incidents', 'N/A')}
            - Produtividade por Hectare: {performance_data.get('yield_per_ha', 'N/A')} ton/ha
            
            BENCHMARKS:
            {performance_data.get('benchmarks', 'N/A')}
            
            Forneça uma análise abrangente em português:
            
            📊 AVALIAÇÃO GERAL:
            - Classificação de desempenho (excelente/bom/regular/precisa melhorar)
            - Resumo executivo
            
            ✅ PONTOS FORTES:
            - Sucessos e conquistas
            - O que está funcionando bem
            
            ⚠️ ÁREAS PARA MELHORIA:
            - Problemas identificados
            - Oportunidades de otimização
            
            📈 COMPARAÇÃO:
            - Vs. benchmarks do setor
            - Vs. períodos anteriores
            - Tendências observadas
            
            💡 INSIGHTS PRINCIPAIS:
            - Padrões e descobertas importantes
            
            🎯 RECOMENDAÇÕES ESTRATÉGICAS:
            - Ações prioritárias para o próximo período
            - Oportunidades de eficiência
            - Prioridades de investimento
            
            Use dados concretos e seja específico nas recomendações.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.7)
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
            ⚠️ EMERGÊNCIA AGRÍCOLA - RESPOSTA IMEDIATA NECESSÁRIA
            
            TIPO DE EMERGÊNCIA: {emergency_type}
            DETALHES: {details}
            
            Forneça um plano de resposta de emergência URGENTE em português:
            
            🚨 AÇÕES IMEDIATAS (próximas 1-4 horas):
            - O que fazer AGORA
            - Prioridade máxima
            
            ⏰ AÇÕES DE CURTO PRAZO (próximas 24-48 horas):
            - Sequência de ações
            - Timeline detalhado
            
            🛠️ RECURSOS NECESSÁRIOS COM URGÊNCIA:
            - Equipamentos
            - Pessoas
            - Insumos
            - Contatos importantes
            
            📉 AVALIAÇÃO DE IMPACTO:
            - Danos esperados se não agir
            - Áreas/culturas afetadas
            - Perdas estimadas
            
            🛡️ PREVENÇÃO DE MAIS DANOS:
            - Como conter a situação
            - Proteção de outras áreas
            
            💊 PLANO DE RECUPERAÇÃO:
            - Passos para recuperação
            - Timeline estimado
            
            📋 ESTRATÉGIAS DE MITIGAÇÃO FUTURAS:
            - Como evitar que aconteça novamente
            - Sistemas de alerta a implementar
            
            🆘 CONTATOS E RECURSOS:
            - Quem chamar
            - Onde buscar ajuda
            
            IMPORTANTE: 
            - Priorize a segurança de pessoas e animais
            - Seja EXTREMAMENTE específico e prático
            - Indique urgência claramente
            - Considere condições e recursos brasileiros
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.5,  # Mais determinístico para emergências
                    max_output_tokens=2048
                )
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
