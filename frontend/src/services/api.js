/**
 * API Service - Centraliza todas as chamadas para o backend
 * AgriSmart Brasil
 */

// Configuração da URL base do backend
const API_BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8080'

/**
 * Função auxiliar para fazer requisições HTTP
 */
async function fetchAPI(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`
  
  const defaultOptions = {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  }
  
  const config = {
    ...defaultOptions,
    ...options,
    headers: {
      ...defaultOptions.headers,
      ...options.headers,
    },
  }
  
  try {
    const response = await fetch(url, config)
    
    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Erro desconhecido' }))
      throw new Error(error.detail || `HTTP error! status: ${response.status}`)
    }
    
    return await response.json()
  } catch (error) {
    console.error('API Error:', error)
    throw error
  }
}

/**
 * ===== CLIMATE MONITOR APIs =====
 */
export const climateAPI = {
  // Analisar clima
  analyze: async (location, climateData) => {
    return fetchAPI('/api/climate/analyze', {
      method: 'POST',
      body: JSON.stringify({ location, climate_data: climateData }),
    })
  },
  
  // Recomendações de irrigação baseadas no clima
  getIrrigationRecommendation: async (climateData, cropType) => {
    return fetchAPI('/api/climate/irrigation-recommendation', {
      method: 'POST',
      body: JSON.stringify({ climate_data: climateData, crop_type: cropType }),
    })
  },
  
  // Impacto do clima
  predictWeatherImpact: async (forecastData, cropStage) => {
    return fetchAPI('/api/climate/weather-impact', {
      method: 'POST',
      body: JSON.stringify({ forecast_data: forecastData, crop_stage: cropStage }),
    })
  },
  
  // ⭐ Risco de geada (NOVO - crítico para Brasil)
  assessFrostRisk: async (location, minTempForecast, cropStage, cropType = 'Soja') => {
    return fetchAPI('/api/weather/frost-risk', {
      method: 'POST',
      body: JSON.stringify({
        location,
        min_temp_forecast: minTempForecast,
        crop_stage: cropStage,
        crop_type: cropType,
      }),
    })
  },
  
  // Avaliação de seca
  assessDrought: async (location, rainfallHistory, soilMoisture, cropType = 'Soja') => {
    return fetchAPI('/api/climate/drought-assessment', {
      method: 'POST',
      body: JSON.stringify({
        location,
        rainfall_history: rainfallHistory,
        soil_moisture: soilMoisture,
        crop_type: cropType,
      }),
    })
  },
}

/**
 * ===== CROP ANALYZER APIs =====
 */
export const cropAPI = {
  // Analisar imagem de cultura
  analyzeImage: async (imageData, cropType, additionalInfo) => {
    return fetchAPI('/api/crop/analyze-image', {
      method: 'POST',
      body: JSON.stringify({
        image_data: imageData,
        crop_type: cropType,
        additional_info: additionalInfo,
      }),
    })
  },
  
  // Upload de imagem
  uploadImage: async (file, cropType = 'unknown') => {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('crop_type', cropType)
    
    return fetchAPI('/api/crop/upload-image', {
      method: 'POST',
      body: formData,
      headers: {}, // Remove Content-Type para multipart/form-data
    })
  },
  
  // Identificar doença
  identifyDisease: async (symptoms, cropType) => {
    return fetchAPI('/api/crop/identify-disease', {
      method: 'POST',
      body: JSON.stringify({ symptoms, crop_type: cropType }),
    })
  },
  
  // Avaliar deficiência de nutrientes
  assessNutrients: async (observations, cropType) => {
    return fetchAPI('/api/crop/nutrient-assessment', {
      method: 'POST',
      body: JSON.stringify({ observations, crop_type: cropType }),
    })
  },
  
  // Recomendações de rotação de culturas
  recommendRotation: async (currentCrop, soilCondition, previousCrops) => {
    return fetchAPI('/api/crop/rotation-recommendation', {
      method: 'POST',
      body: JSON.stringify({
        current_crop: currentCrop,
        soil_condition: soilCondition,
        previous_crops: previousCrops,
      }),
    })
  },
}

/**
 * ===== WATER OPTIMIZER APIs =====
 */
export const waterAPI = {
  // Criar cronograma de irrigação
  createSchedule: async (cropType, fieldSize, soilType, climateData, waterAvailability) => {
    return fetchAPI('/api/water/irrigation-schedule', {
      method: 'POST',
      body: JSON.stringify({
        crop_type: cropType,
        field_size: fieldSize,
        soil_type: soilType,
        climate_data: climateData,
        water_availability: waterAvailability,
      }),
    })
  },
  
  // Calcular eficiência hídrica
  calculateEfficiency: async (waterUsed, fieldSize, cropYield, cropType) => {
    return fetchAPI('/api/water/efficiency', {
      method: 'POST',
      body: JSON.stringify({
        water_used: waterUsed,
        field_size: fieldSize,
        crop_yield: cropYield,
        crop_type: cropType,
      }),
    })
  },
  
  // Detectar problemas de irrigação
  detectIssues: async (sensorData, irrigationSystem) => {
    return fetchAPI('/api/water/detect-issues', {
      method: 'POST',
      body: JSON.stringify({
        sensor_data: sensorData,
        irrigation_system: irrigationSystem,
      }),
    })
  },
  
  // Recomendar tecnologia de irrigação
  recommendTechnology: async (farmDetails, budget, waterSource) => {
    return fetchAPI('/api/water/technology-recommendation', {
      method: 'POST',
      body: JSON.stringify({
        farm_details: farmDetails,
        budget,
        water_source: waterSource,
      }),
    })
  },
}

/**
 * ===== YIELD PREDICTOR APIs =====
 */
export const yieldAPI = {
  // Prever produção
  predict: async (cropType, fieldSize, plantingDate, currentConditions, historicalData = null) => {
    return fetchAPI('/api/yield/predict', {
      method: 'POST',
      body: JSON.stringify({
        crop_type: cropType,
        field_size: fieldSize,
        planting_date: plantingDate,
        current_conditions: currentConditions,
        historical_data: historicalData,
      }),
    })
  },
  
  // Analisar lacunas de produção
  analyzeGaps: async (actualYield, potentialYield, cropType, farmingPractices) => {
    return fetchAPI('/api/yield/gap-analysis', {
      method: 'POST',
      body: JSON.stringify({
        actual_yield: actualYield,
        potential_yield: potentialYield,
        crop_type: cropType,
        farming_practices: farmingPractices,
      }),
    })
  },
  
  // Timing de mercado
  forecastMarketTiming: async (cropType, expectedHarvestDate, expectedQuantity, marketData) => {
    return fetchAPI('/api/yield/market-timing', {
      method: 'POST',
      body: JSON.stringify({
        crop_type: cropType,
        expected_harvest_date: expectedHarvestDate,
        expected_quantity: expectedQuantity,
        market_data: marketData,
      }),
    })
  },
  
  // Otimizar cronograma de plantio
  optimizePlantingSchedule: async (crops, fieldSize, climateZone, objectives) => {
    return fetchAPI('/api/yield/planting-schedule', {
      method: 'POST',
      body: JSON.stringify({
        crops,
        field_size: fieldSize,
        climate_zone: climateZone,
        objectives,
      }),
    })
  },
}

/**
 * ===== FARM MANAGER APIs =====
 */
export const farmAPI = {
  // Briefing diário
  getDailyBriefing: async (farmData) => {
    return fetchAPI('/api/farm/daily-briefing', {
      method: 'POST',
      body: JSON.stringify({ farm_data: farmData }),
    })
  },
  
  // Chat com agentes (PRINCIPAL)
chat: async (query, context) => {
  return fetchAPI('/api/farm/query', {
    method: 'POST',
    body: JSON.stringify({ 
      query: query,
      context: context || {
        location: 'Cascavel, PR',
        farm_size: '500 hectares',
        crops: ['soja', 'milho'],
        crop_stage: 'floração'
      }
    }),
  })
},


  
  // Criar plano de ação
  createActionPlan: async (goal, timeframe, farmStatus, constraints = null) => {
    return fetchAPI('/api/farm/action-plan', {
      method: 'POST',
      body: JSON.stringify({
        goal,
        timeframe,
        farm_status: farmStatus,
        constraints,
      }),
    })
  },
  
  // Analisar desempenho
  analyzePerformance: async (performanceData, period) => {
    return fetchAPI('/api/farm/performance', {
      method: 'POST',
      body: JSON.stringify({
        performance_data: performanceData,
        period,
      }),
    })
  },
  
  // Emergência
  handleEmergency: async (emergencyType, details) => {
    return fetchAPI('/api/farm/emergency', {
      method: 'POST',
      body: JSON.stringify({
        emergency_type: emergencyType,
        details,
      }),
    })
  },
}

/**
 * ===== GENERAL APIs =====
 */
export const generalAPI = {
  // Health check
  healthCheck: async () => {
    return fetchAPI('/health')
  },
  
  // Listar agentes
  listAgents: async () => {
    return fetchAPI('/api/agents')
  },
}

// Exportar tudo como default também
export default {
  climate: climateAPI,
  crop: cropAPI,
  water: waterAPI,
  yield: yieldAPI,
  farm: farmAPI,
  general: generalAPI,
}

