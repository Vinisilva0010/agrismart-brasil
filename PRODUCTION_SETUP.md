# 🚀 Setup de Produção - AgriSmart Brasil

## ✅ Backend já está no ar!

**URL do Backend**: https://agrismart-backend-305905232437.southamerica-east1.run.app

### Teste se está funcionando:
```bash
curl https://agrismart-backend-305905232437.southamerica-east1.run.app/health
```

Deve retornar:
```json
{
  "status": "healthy",
  "service": "agrismart-brasil"
}
```

---

## 🎨 Configurar Frontend para Produção

### 1. Criar arquivo `.env.local` na pasta frontend

```bash
cd frontend
```

Crie o arquivo `.env.local` com:
```env
VITE_BACKEND_URL=https://agrismart-backend-305905232437.southamerica-east1.run.app
VITE_ENV=production
```

**OU** no Windows CMD:
```cmd
cd frontend
echo VITE_BACKEND_URL=https://agrismart-backend-305905232437.southamerica-east1.run.app > .env.local
echo VITE_ENV=production >> .env.local
```

### 2. Testar Localmente

```bash
npm run dev
```

Acesse: http://localhost:5173

O frontend vai conectar com o backend em produção!

### 3. Build para Produção

```bash
npm run build
```

### 4. Preview do Build

```bash
npm run preview
```

---

## ☁️ Deploy do Frontend no Cloud Run

### Opção 1: Deploy Automático

```bash
cd frontend

# Build e push da imagem
gcloud builds submit --tag gcr.io/PROJECT_ID/agrismart-frontend

# Deploy no Cloud Run
gcloud run deploy agrismart-frontend \
  --image gcr.io/PROJECT_ID/agrismart-frontend \
  --platform managed \
  --region southamerica-east1 \
  --allow-unauthenticated \
  --set-env-vars VITE_BACKEND_URL=https://agrismart-backend-305905232437.southamerica-east1.run.app
```

### Opção 2: Deploy via Docker

```bash
cd frontend

# Build da imagem localmente
docker build -t agrismart-frontend .

# Tag para Google Container Registry
docker tag agrismart-frontend gcr.io/PROJECT_ID/agrismart-frontend

# Push para GCR
docker push gcr.io/PROJECT_ID/agrismart-frontend

# Deploy no Cloud Run
gcloud run deploy agrismart-frontend \
  --image gcr.io/PROJECT_ID/agrismart-frontend \
  --platform managed \
  --region southamerica-east1 \
  --allow-unauthenticated
```

---

## 🔧 Configuração CORS no Backend

Se você tiver problemas de CORS, atualize o backend:

```bash
gcloud run services update agrismart-backend \
  --set-env-vars CORS_ORIGINS=https://your-frontend-url.run.app \
  --region southamerica-east1
```

---

## 📊 URLs de Produção

| Serviço | URL |
|---------|-----|
| **Backend API** | https://agrismart-backend-305905232437.southamerica-east1.run.app |
| **API Docs** | https://agrismart-backend-305905232437.southamerica-east1.run.app/api/docs |
| **Health Check** | https://agrismart-backend-305905232437.southamerica-east1.run.app/health |
| **Frontend** | (será criado após deploy) |

---

## 🧪 Testar Endpoints do Backend

### Health Check
```bash
curl https://agrismart-backend-305905232437.southamerica-east1.run.app/health
```

### Listar Agentes
```bash
curl https://agrismart-backend-305905232437.southamerica-east1.run.app/api/agents
```

### Chat com Farm Manager
```bash
curl -X POST https://agrismart-backend-305905232437.southamerica-east1.run.app/api/farm/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Qual a melhor época para plantar soja?",
    "context": {
      "location": "São Paulo, Brasil",
      "crops": ["Soja"],
      "season": "Safra 2024/2025"
    }
  }'
```

### Análise de Clima
```bash
curl -X POST https://agrismart-backend-305905232437.southamerica-east1.run.app/api/climate/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "location": "Brasília, DF",
    "climate_data": {
      "temperature": 28,
      "humidity": 60,
      "rainfall": 5
    }
  }'
```

### Risco de Geada (NOVO!)
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

## 🎯 Checklist de Deploy

- [x] Backend no Cloud Run
- [x] Backend Health Check OK
- [x] Backend API Docs acessível
- [ ] Frontend `.env.local` configurado
- [ ] Frontend testado localmente
- [ ] Frontend build criado
- [ ] Frontend no Cloud Run
- [ ] CORS configurado
- [ ] URLs atualizadas no README

---

## 🐛 Troubleshooting

### Erro: CORS blocked

**Solução**: Atualizar CORS_ORIGINS no backend:
```bash
gcloud run services update agrismart-backend \
  --set-env-vars CORS_ORIGINS=* \
  --region southamerica-east1
```

### Erro: Backend não responde

**Solução**: Verificar logs:
```bash
gcloud run services logs read agrismart-backend --region southamerica-east1
```

### Erro: Frontend não conecta

**Verificar**:
1. Arquivo `.env.local` existe?
2. URL do backend está correta?
3. Backend está respondendo?

---

## 📞 Suporte

- **API Docs**: https://agrismart-backend-305905232437.southamerica-east1.run.app/api/docs
- **GitHub**: https://github.com/Vinisilva0010/agrismart-brasil
- **Logs Backend**: `gcloud run services logs read agrismart-backend --region southamerica-east1`

---

**Boa sorte com o deploy! 🚀🌾**

