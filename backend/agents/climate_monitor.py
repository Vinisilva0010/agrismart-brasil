"""
Climate Monitor Agent
Monitora condições climáticas e fornece insights para agricultura brasileira.
"""

import os
from typing import Dict, Any, List
from google import genai
from google.genai import types


class ClimateMonitorAgent:
    """Agente responsável por monitorar clima e condições meteorológicas."""
    
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
            Você é um especialista em meteorologia agrícola brasileira.
            
            Analise os dados climáticos para uma fazenda em {location}:
            
            🌡️ Temperatura: {climate_data.get('temperature', 'N/A')}°C
            💧 Umidade: {climate_data.get('humidity', 'N/A')}%
            🌧️ Precipitação: {climate_data.get('rainfall', 'N/A')}mm
            💨 Velocidade do Vento: {climate_data.get('wind_speed', 'N/A')} km/h
            ☀️ Índice UV: {climate_data.get('uv_index', 'N/A')}
            
            Forneça em português brasileiro:
            
            📊 AVALIAÇÃO DAS CONDIÇÕES ATUAIS:
            - Classificação geral do clima (ideal/bom/adequado/adverso)
            - Como está em relação ao esperado para a região e época
            
            ⚠️ FATORES DE RISCO PARA CULTURAS:
            - Riscos imediatos identificados
            - Culturas mais vulneráveis
            - Nível de preocupação (baixo/médio/alto/crítico)
            
            ✅ RECOMENDAÇÕES IMEDIATAS:
            - Ações para hoje
            - Prioridades de manejo
            - Cuidados especiais
            
            📅 PERSPECTIVA DE 7 DIAS:
            - Tendências esperadas
            - Planejamento de atividades
            - Janelas de oportunidade
            
            Use linguagem clara e objetiva, com foco em ações práticas.
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
            Como especialista em irrigação agrícola, recomende estratégia de irrigação para {crop_type}:
            
            Temperatura: {climate_data.get('temperature', 'N/A')}°C
            Umidade: {climate_data.get('humidity', 'N/A')}%
            Chuva Recente: {climate_data.get('rainfall', 'N/A')}mm
            Umidade do Solo: {climate_data.get('soil_moisture', 'N/A')}%
            
            Forneça recomendações específicas em português:
            
            💧 DECISÃO DE IRRIGAÇÃO:
            - Irrigar hoje? (SIM/NÃO)
            - Justificativa da decisão
            
            📊 VOLUME DE ÁGUA:
            - Quantidade recomendada (litros por hectare)
            - Baseado em quê
            
            ⏰ TIMING IDEAL:
            - Melhor horário do dia
            - Duração estimada
            - Por que esse horário
            
            💡 OBSERVAÇÕES:
            - Condições especiais a considerar
            - Dicas de eficiência
            - Economia de água
            
            Seja específico e prático nas recomendações.
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
            Analise o impacto da previsão meteorológica em culturas no estágio {crop_stage}:
            
            Previsão: {forecast_data}
            
            Forneça análise em português:
            
            ✅ IMPACTOS POSITIVOS:
            - Benefícios esperados do clima previsto
            - Oportunidades a aproveitar
            
            ⚠️ IMPACTOS NEGATIVOS:
            - Riscos identificados
            - Possíveis problemas
            
            🛡️ MEDIDAS PREVENTIVAS:
            - Ações para minimizar riscos
            - Timeline de implementação
            
            💡 RECOMENDAÇÕES DE OPORTUNIDADE:
            - Como aproveitar condições favoráveis
            - Atividades recomendadas
            
            Considere as condições agrícolas brasileiras.
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
    
    async def get_frost_risk(
        self,
        location: str,
        min_temp_forecast: float,
        crop_stage: str,
        crop_type: str = "Soja"
    ) -> Dict[str, Any]:
        """
        Avaliar risco de geada para culturas.
        
        Args:
            location: Localização da fazenda
            min_temp_forecast: Temperatura mínima prevista em °C
            crop_stage: Estágio atual da cultura
            crop_type: Tipo de cultura
            
        Returns:
            Avaliação de risco de geada e recomendações
        """
        try:
            prompt = f"""
            Você é um especialista em meteorologia agrícola brasileira.
            
            Avalie o risco de GEADA para esta situação:
            
            📍 Localização: {location}
            🌡️ Temperatura Mínima Prevista: {min_temp_forecast}°C
            🌾 Cultura: {crop_type}
            📊 Estágio de Crescimento: {crop_stage}
            
            Forneça uma análise completa em português brasileiro:
            
            🌡️ ANÁLISE DE RISCO:
            - Nível de risco: CRÍTICO / ALTO / MÉDIO / BAIXO / NENHUM
            - Temperatura crítica para {crop_type}: __°C
            - Diferença para temperatura prevista: __°C
            - Probabilidade de geada: __%
            
            ⚠️ IMPACTOS POTENCIAIS:
            - Danos esperados se ocorrer geada
            - Partes da planta mais vulneráveis
            - Perdas estimadas de produtividade (%)
            - Danos reversíveis vs. permanentes
            
            🛡️ MEDIDAS PREVENTIVAS URGENTES:
            - Ações para fazer ANTES da geada (próximas 12-24h)
            - Métodos de proteção recomendados:
              * Irrigação preventiva
              * Cobertura ou proteção física
              * Ventiladores ou aquecedores
              * Queima controlada (se aplicável)
            - Custo vs benefício de cada medida
            - Priorização de áreas
            
            📅 TIMELINE:
            - Quando esperar a temperatura mais baixa
            - Duração esperada do risco
            - Quando reavaliar a situação
            
            ✅ AÇÕES PÓS-GEADA (se ocorrer):
            - Como avaliar danos nas primeiras horas
            - Medidas de recuperação imediatas
            - O que NÃO fazer
            
            💡 RECOMENDAÇÕES ESPECÍFICAS PARA O BRASIL:
            - Práticas comuns na região
            - Recursos disponíveis localmente
            - Experiências de produtores vizinhos
            
            IMPORTANTE: Seja EXTREMAMENTE específico e prático. Priorize ações 
            que podem ser tomadas COM OS RECURSOS DISPONÍVEIS no Brasil.
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "climate_monitor",
                "frost_risk": {
                    "location": location,
                    "min_temp_forecast": min_temp_forecast,
                    "crop_type": crop_type,
                    "crop_stage": crop_stage,
                    "analysis": response.text
                }
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "climate_monitor",
                "error": str(e)
            }
    
    async def drought_assessment(
        self,
        location: str,
        rainfall_history: List[float],
        soil_moisture: float,
        crop_type: str = "Soja"
    ) -> Dict[str, Any]:
        """
        Avaliar condições de seca e impactos nas culturas.
        
        Args:
            location: Localização da fazenda
            rainfall_history: Histórico de chuvas dos últimos 30-60 dias (mm)
            soil_moisture: Umidade atual do solo (%)
            crop_type: Tipo de cultura
            
        Returns:
            Avaliação de seca e estratégias de mitigação
        """
        try:
            total_rainfall = sum(rainfall_history)
            days_tracked = len(rainfall_history)
            avg_rainfall = total_rainfall / days_tracked if days_tracked > 0 else 0
            
            prompt = f"""
            Você é um especialista em recursos hídricos e agricultura de precisão no Brasil.
            
            Avalie as condições de SECA para esta fazenda:
            
            📍 Localização: {location}
            🌾 Cultura: {crop_type}
            🌧️ Chuva Total (últimos {days_tracked} dias): {total_rainfall}mm
            📊 Chuva Média Diária: {avg_rainfall:.1f}mm
            💧 Umidade do Solo Atual: {soil_moisture}%
            
            Forneça uma avaliação completa em português brasileiro:
            
            💧 CLASSIFICAÇÃO DA SECA:
            - Severidade: EXTREMA / SEVERA / MODERADA / LEVE / NORMAL
            - Comparação com níveis normais para {location} nesta época
            - Tendência (melhorando / piorando / estável)
            - Previsão de agravamento ou melhora
            
            📊 ANÁLISE DETALHADA DE DADOS:
            - Déficit hídrico acumulado
            - Dias consecutivos sem chuva significativa (>5mm)
            - Umidade do solo vs. ideal para {crop_type}
            - Índice de estresse hídrico da cultura
            - Capacidade de recuperação do solo
            
            🌾 IMPACTOS NA CULTURA:
            - Estágio de crescimento mais afetado
            - Perdas de produtividade estimadas (%)
            - Sinais visíveis de estresse hídrico a observar:
              * Folhas murchas ou enroladas
              * Amarelamento
              * Crescimento reduzido
              * Flores ou frutos abortados
            - Danos já ocorridos vs. ainda evitáveis
            - Tempo para recuperação com irrigação
            
            💦 ESTRATÉGIAS DE IRRIGAÇÃO PRIORITÁRIAS:
            - Volume de água necessário (litros/ha/dia)
            - Frequência ideal de irrigação
            - Método de irrigação mais eficiente:
              * Aspersão
              * Gotejamento
              * Pivô central
            - Priorização de áreas (talhões mais críticos)
            - Manejo do déficit hídrico (PRD, RDI)
            
            🌱 MANEJO AGRÍCOLA PARA MITIGAR SECA:
            - Ajustes na adubação (reduzir N, manter K)
            - Controle rigoroso de plantas daninhas
            - Proteção de solo:
              * Mulching
              * Cobertura morta
              * Plantio direto
            - Redução de perdas por evaporação
            - Quebra-ventos
            
            📅 PLANEJAMENTO E MONITORAMENTO:
            - Indicadores para monitorar diariamente
            - Gatilhos para ações emergenciais
            - Quando reavaliar a situação
            - Previsão de chuvas (se disponível)
            
            💰 ANÁLISE ECONÔMICA:
            - Custo da irrigação emergencial
            - Custo da perda de produção sem irrigar
            - ROI de diferentes estratégias
            - Viabilidade de poços, açudes, captação
            - Opções de seguro agrícola disponíveis
            
            🌦️ PREPARAÇÃO PARA O FUTURO:
            - Investimentos em infraestrutura hídrica:
              * Sistemas de irrigação
              * Reservatórios
              * Poços artesianos
              * Captação de água da chuva
            - Culturas mais resistentes à seca
            - Variedades tolerantes ao estresse hídrico
            - Rotação de culturas
            
            🇧🇷 CONTEXTO BRASILEIRO ESPECÍFICO:
            - Programas governamentais de apoio disponíveis
            - Tecnologias acessíveis no Brasil
            - Práticas sustentáveis de gestão hídrica
            - Experiências de sucesso na região
            
            IMPORTANTE: 
            - Seja MUITO específico em números e prazos
            - Considere a realidade econômica do produtor brasileiro
            - Priorize soluções viáveis e implementáveis
            - Foque em AÇÕES CONCRETAS que podem ser tomadas AGORA
            """
            
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            return {
                "status": "success",
                "agent": "climate_monitor",
                "drought_assessment": {
                    "location": location,
                    "total_rainfall": total_rainfall,
                    "days_tracked": days_tracked,
                    "avg_rainfall": avg_rainfall,
                    "soil_moisture": soil_moisture,
                    "crop_type": crop_type,
                    "analysis": response.text
                }
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent": "climate_monitor",
                "error": str(e)
            }
