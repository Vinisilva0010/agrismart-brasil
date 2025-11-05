# 🌐 AgriSmart Brasil - URLs de Produção

## ✅ SISTEMA COMPLETAMENTE DEPLOYADO!

Data de Deploy: 05 de Novembro de 2025
Região: South America East 1 (São Paulo, Brasil)

---

## 🚀 URLs Principais

### Frontend (Interface do Usuário)
**URL**: https://agrismart-frontend-305905232437.southamerica-east1.run.app

**Acesse para**:
- Dashboard com métricas da fazenda
- Chat com agentes de IA
- Upload e análise de imagens de culturas
- Briefings diários gerados por IA

---

### Backend (API)
**URL Base**: https://agrismart-backend-305905232437.southamerica-east1.run.app

**Endpoints Principais**:
- 🏥 Health Check: `/health`
- 📚 Documentação Interativa: `/api/docs`
- 📖 ReDoc: `/api/redoc`
- 📋 Listar Agentes: `/api/agents`

---

## 🤖 Agentes Disponíveis

### 1. Climate Monitor (Monitor Climático)
- `POST /api/climate/analyze` - Analisar condições climáticas
- `POST /api/climate/irrigation-recommendation` - Recomendações de irrigação
- `POST /api/climate/weather-impact` - Impacto do clima
- `POST /api/weather/frost-risk` ⭐ - **Risco de geada** (NOVO!)
- `POST /api/climate/drought-assessment` ⭐ - **Avaliação de seca** (NOVO!)

### 2. Crop Analyzer (Analisador de Culturas)
- `POST /api/crop/analyze-image` - Analisar imagem (base64)
- `POST /api/crop/upload-image` - Upload de imagem (multipart)
- `POST /api/crop/identify-disease` - Identificar doença
- `POST /api/crop/nutrient-assessment` - Avaliar nutrientes
- `POST /api/crop/rotation-recommendation` - Rotação de culturas

### 3. Water Optimizer (Otimizador de Água)
- `POST /api/water/irrigation-schedule` - Cronograma de irrigação
- `POST /api/water/efficiency` - Eficiência hídrica
- `POST /api/water/detect-issues` - Detectar problemas
- `POST /api/water/technology-recommendation` - Recomendar tecnologia

### 4. Yield Predictor (Preditor de Produção)
- `POST /api/yield/predict` - Prever produção
- `POST /api/yield/gap-analysis` - Análise de lacunas
- `POST /api/yield/market-timing` - Timing de mercado
- `POST /api/yield/planting-schedule` - Cronograma de plantio

### 5. Farm Manager (Gestor da Fazenda) - ORQUESTRADOR
- `POST /api/farm/query` ⭐ - **Chat principal** (coordena todos os agentes)
- `POST /api/farm/daily-briefing` - Briefing diário
- `POST /api/farm/action-plan` - Criar plano de ação
- `POST /api/farm/performance` - Análise de desempenho
- `POST /api/farm/emergency` - Gestão de emergências

---

## 🧪 Testes Rápidos

### 1. Teste o Frontend
Abra no navegador:
```
https://agrismart-frontend-305905232437.southamerica-east1.run.app
```

Você verá a interface do AgriSmart Brasil!

### 2. Teste a API (Backend)
```bash
# Health Check
curl https://agrismart-backend-305905232437.southamerica-east1.run.app/health

# Listar Agentes
curl https://agrismart-backend-305905232437.southamerica-east1.run.app/api/agents
```

### 3. Teste o Chat (Principal Feature)
```bash
curl -X POST https://agrismart-backend-305905232437.southamerica-east1.run.app/api/farm/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Qual a melhor época para plantar soja no Brasil?",
    "context": {
      "location": "São Paulo, Brasil",
      "crops": ["Soja"],
      "season": "Safra 2024/2025"
    }
  }'
```

### 4. Teste Risco de Geada (Novo Endpoint)
```bash
curl -X POST https://agrismart-backend-305905232437.southamerica-east1.run.app/api/weather/frost-risk \
  -H "Content-Type: application/json" \
  -d '{
    "location": "Paraná, Brasil",
    "min_temp_forecast": 2.5,
    "crop_stage": "Floração",
    "crop_type": "Soja"
  }'
```

---

## 📊 Status dos Serviços

| Serviço | Status | URL |
|---------|--------|-----|
| **Frontend** | ✅ **ONLINE** | https://agrismart-frontend-305905232437.southamerica-east1.run.app |
| **Backend** | ✅ **ONLINE** | https://agrismart-backend-305905232437.southamerica-east1.run.app |
| **API Docs** | ✅ **ONLINE** | https://agrismart-backend-305905232437.southamerica-east1.run.app/api/docs |
| **GitHub** | ✅ **ONLINE** | https://github.com/Vinisilva0010/agrismart-brasil |

---

## 🎯 Funcionalidades Deployadas

✅ **5 Agentes de IA** especializados com Gemini 2.0 Flash
✅ **28 Endpoints** de API documentados
✅ **Interface React** moderna e responsiva
✅ **Chat em tempo real** com coordenação multi-agente
✅ **Análise de imagens** para diagnóstico de culturas
✅ **Briefings diários** automatizados
✅ **Totalmente em português brasileiro**
✅ **Deploy automático** no Google Cloud Run
✅ **Documentação completa** da API

---

## 🎓 Para o Hackathon

### Diferenciais do Projeto:
1. ✅ **Multi-Agente Real** - 5 agentes especializados
2. ✅ **Gemini 2.0 Flash** - Modelo mais recente
3. ✅ **Problema Real** - Agricultura brasileira
4. ✅ **Completo** - Backend + Frontend + Deploy
5. ✅ **Documentação** - README, QUICKSTART, DEPLOYMENT
6. ✅ **Open Source** - GitHub público
7. ✅ **Produção** - Sistema totalmente funcional
8. ✅ **Português** - Interface e respostas em PT-BR
9. ✅ **Específico para Brasil** - Culturas, clima, práticas locais

### Endpoints Críticos para Demo:
- `/api/farm/query` - Chat principal ⭐
- `/api/weather/frost-risk` - Risco de geada ⭐
- `/api/crop/upload-image` - Análise de imagem ⭐
- `/api/farm/daily-briefing` - Briefing diário ⭐

---

## 🎮 Como Demonstrar

### 1. Abra o Frontend
https://agrismart-frontend-305905232437.southamerica-east1.run.app

### 2. Use o Chat
- Digite: "Qual a melhor época para plantar soja?"
- Mostra: Coordenação multi-agente em ação

### 3. Faça Upload de Imagem
- Aba "Analisar Cultura"
- Upload de foto de planta
- Mostra: Gemini Vision analisando culturas

### 4. Gere um Briefing
- Aba "Dashboard"
- Botão "Gerar Briefing"
- Mostra: Insights diários automatizados

---

## 🔐 Segurança

- ✅ HTTPS em todos os serviços
- ✅ Headers de segurança configurados
- ✅ CORS controlado
- ✅ API Key não exposta no frontend
- ✅ Health checks ativos
- ✅ .env files não commitados no git

---

## 💰 Custos Estimados

Com uso moderado do hackathon:
- Cloud Run Frontend: ~$0-5/mês (tier gratuito)
- Cloud Run Backend: ~$0-10/mês (tier gratuito)
- Google AI (Gemini): ~$0-20/mês (tier gratuito até certo ponto)

**Total: Essencialmente GRATUITO durante desenvolvimento e demo!**

---

## 📞 Informações de Suporte

- **Logs Frontend**: `gcloud run services logs read agrismart-frontend --region southamerica-east1`
- **Logs Backend**: `gcloud run services logs read agrismart-backend --region southamerica-east1`
- **Projeto GCP**: agrismart-hackathon
- **Região**: southamerica-east1 (São Paulo, Brasil)

---

**Sistema 100% Funcional e Pronto para o Hackathon! 🚀🌾**

Data: 05/11/2025
Status: ✅ PRODUÇÃO

