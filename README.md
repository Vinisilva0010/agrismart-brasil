# 🌾 AgriSmart Brasil

Sistema Multi-Agente para Agricultura Inteligente usando Google Gemini 2.0 Flash

## 🌐 URLs de Produção

- **Backend API**: https://agrismart-backend-305905232437.southamerica-east1.run.app
- **API Docs**: https://agrismart-backend-305905232437.southamerica-east1.run.app/api/docs
- **Health Check**: https://agrismart-backend-305905232437.southamerica-east1.run.app/health
- **GitHub**: https://github.com/Vinisilva0010/agrismart-brasil

## 📋 Visão Geral

AgriSmart Brasil é uma plataforma completa de gestão agrícola que utiliza inteligência artificial multi-agente para fornecer insights precisos e recomendações acionáveis para agricultores brasileiros.

### 🤖 Agentes Especializados

1. **Climate Monitor** (Monitor Climático)
   - Análise de condições climáticas
   - Recomendações de irrigação baseadas no clima
   - Previsão de impacto do tempo nas culturas

2. **Crop Analyzer** (Analisador de Culturas)
   - Análise de saúde das culturas via imagem
   - Identificação de doenças e pragas
   - Avaliação de deficiências nutricionais
   - Recomendações de rotação de culturas

3. **Water Optimizer** (Otimizador de Água)
   - Criação de cronogramas de irrigação otimizados
   - Cálculo de eficiência hídrica
   - Detecção de problemas no sistema de irrigação
   - Recomendações de tecnologia de irrigação

4. **Yield Predictor** (Preditor de Produção)
   - Previsão de rendimento de culturas
   - Análise de lacunas de produtividade
   - Recomendações de timing de mercado
   - Otimização de cronograma de plantio

5. **Farm Manager** (Gestor da Fazenda)
   - Coordenação de todos os agentes
   - Briefings diários da fazenda
   - Planos de ação abrangentes
   - Análise de desempenho da fazenda
   - Gestão de emergências

## 🏗️ Arquitetura

```
agrismart-brasil/
├── backend/                 # API FastAPI + Python 3.11
│   ├── agents/             # Agentes especializados
│   ├── api/                # Endpoints FastAPI
│   └── services/           # Serviços (Firestore, etc.)
├── frontend/               # React + Vite + Tailwind
│   └── src/
│       ├── components/     # Componentes React
│       └── App.jsx         # App principal
└── README.md
```

## 🚀 Tecnologias

### Backend
- **FastAPI** - Framework web moderno e rápido
- **Python 3.11** - Linguagem de programação
- **Google Gemini 2.0 Flash** - Modelo de IA para os agentes
- **Google Cloud Firestore** - Banco de dados NoSQL
- **Uvicorn** - Servidor ASGI

### Frontend
- **React 18** - Biblioteca UI
- **Vite** - Build tool e dev server
- **Tailwind CSS** - Framework CSS utility-first
- **Modern JavaScript (ES6+)** - Linguagem

### Deploy
- **Google Cloud Run** - Plataforma serverless
- **Docker** - Containerização

## 📦 Instalação

### Pré-requisitos

- Python 3.11+
- Node.js 20+
- Google Cloud Account
- Google AI API Key

### Backend

```bash
cd backend

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp env.example .env
# Editar .env com suas credenciais

# Executar servidor
uvicorn api.main:app --reload --port 8080
```

### Frontend

```bash
cd frontend

# Instalar dependências
npm install

# Executar em desenvolvimento
npm run dev

# Build para produção
npm run build
```

## 🔑 Configuração

### Variáveis de Ambiente (Backend)

Crie um arquivo `.env` na pasta `backend/`:

```env
GOOGLE_API_KEY=your_google_ai_api_key_here
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account-key.json
PORT=8080
CORS_ORIGINS=http://localhost:5173,https://yourdomain.com
ENVIRONMENT=development
```

### Obter API Key do Google AI

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma nova API Key
3. Copie a chave para o arquivo `.env`

### Configurar Google Cloud Firestore

1. Acesse o [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto ou selecione um existente
3. Ative o Firestore Database
4. Crie uma Service Account e baixe o JSON de credenciais
5. Configure o caminho no `.env`

## 🐳 Deploy com Docker

### Backend

```bash
cd backend

# Build da imagem
docker build -t agrismart-backend .

# Executar container
docker run -p 8080:8080 --env-file .env agrismart-backend
```

### Frontend

```bash
cd frontend

# Build da imagem
docker build -t agrismart-frontend .

# Executar container
docker run -p 8080:8080 agrismart-frontend
```

## ☁️ Deploy no Google Cloud Run

### Backend

```bash
cd backend

# Build e push para Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/agrismart-backend

# Deploy no Cloud Run
gcloud run deploy agrismart-backend \
  --image gcr.io/YOUR_PROJECT_ID/agrismart-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_key_here
```

### Frontend

```bash
cd frontend

# Build e push
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/agrismart-frontend

# Deploy
gcloud run deploy agrismart-frontend \
  --image gcr.io/YOUR_PROJECT_ID/agrismart-frontend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 📚 API Endpoints

### Climate Monitor
- `POST /api/climate/analyze` - Analisar condições climáticas
- `POST /api/climate/irrigation-recommendation` - Recomendações de irrigação
- `POST /api/climate/weather-impact` - Prever impacto do clima

### Crop Analyzer
- `POST /api/crop/analyze-image` - Analisar imagem de cultura
- `POST /api/crop/upload-image` - Upload e análise de imagem
- `POST /api/crop/identify-disease` - Identificar doença
- `POST /api/crop/nutrient-assessment` - Avaliar nutrientes
- `POST /api/crop/rotation-recommendation` - Recomendar rotação

### Water Optimizer
- `POST /api/water/irrigation-schedule` - Criar cronograma de irrigação
- `POST /api/water/efficiency` - Calcular eficiência hídrica
- `POST /api/water/detect-issues` - Detectar problemas
- `POST /api/water/technology-recommendation` - Recomendar tecnologia

### Yield Predictor
- `POST /api/yield/predict` - Prever produção
- `POST /api/yield/gap-analysis` - Analisar lacunas
- `POST /api/yield/market-timing` - Timing de mercado
- `POST /api/yield/planting-schedule` - Otimizar plantio

### Farm Manager
- `POST /api/farm/daily-briefing` - Briefing diário
- `POST /api/farm/query` - Consulta geral
- `POST /api/farm/action-plan` - Criar plano de ação
- `POST /api/farm/performance` - Analisar desempenho
- `POST /api/farm/emergency` - Gerenciar emergência

## 🎯 Funcionalidades

### Dashboard
- Visão geral da fazenda
- Métricas em tempo real
- Briefing diário gerado por IA
- Ações rápidas

### Chat com Agentes
- Interface conversacional
- Consulta a múltiplos agentes
- Respostas contextualizadas
- Histórico de conversas

### Análise de Imagens
- Upload de fotos de culturas
- Detecção de doenças e pragas
- Análise nutricional
- Recomendações de tratamento

## 🔒 Segurança

- CORS configurado
- Validação de entrada com Pydantic
- Variáveis de ambiente para credenciais
- HTTPS no Cloud Run
- Headers de segurança no Nginx

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

AgriSmart Brasil Team

## 🙏 Agradecimentos

- Google AI pela API Gemini 2.0 Flash
- Comunidade FastAPI
- Comunidade React
- Todos os agricultores brasileiros que inspiram este projeto

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato via email.

---

**Feito com ❤️ para a agricultura brasileira** 🇧🇷

