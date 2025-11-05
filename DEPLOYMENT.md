# 🚀 Guia de Deploy - AgriSmart Brasil

Este guia fornece instruções detalhadas para fazer o deploy do AgriSmart Brasil no Google Cloud Run.

## 📋 Pré-requisitos

1. **Google Cloud Account**
   - Conta ativa no Google Cloud
   - Projeto criado no Google Cloud Console
   - Billing habilitado

2. **Ferramentas Instaladas**
   - [Google Cloud SDK (gcloud)](https://cloud.google.com/sdk/docs/install)
   - Docker Desktop
   - Git

3. **Credenciais**
   - Google AI API Key ([obter aqui](https://makersuite.google.com/app/apikey))
   - Google Cloud Service Account (opcional, para Firestore)

## 🔧 Configuração Inicial

### 1. Autenticar no Google Cloud

```bash
# Login
gcloud auth login

# Configurar projeto
gcloud config set project YOUR_PROJECT_ID

# Autenticar Docker
gcloud auth configure-docker
```

### 2. Habilitar APIs Necessárias

```bash
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  containerregistry.googleapis.com \
  artifactregistry.googleapis.com \
  firestore.googleapis.com
```

### 3. Criar Firestore Database

```bash
# Criar database no modo nativo
gcloud firestore databases create --region=us-central1
```

## 🐳 Deploy com Script Automatizado

A forma mais fácil é usar o script de deploy:

```bash
# Tornar o script executável (Linux/Mac)
chmod +x deploy.sh

# Executar deploy
./deploy.sh
```

O script irá:
1. Verificar pré-requisitos
2. Habilitar APIs necessárias
3. Fazer build do backend
4. Deploy do backend no Cloud Run
5. Fazer build do frontend
6. Deploy do frontend no Cloud Run
7. Exibir as URLs dos serviços

## 📦 Deploy Manual

### Backend

```bash
cd backend

# Build da imagem
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/agrismart-backend

# Deploy no Cloud Run
gcloud run deploy agrismart-backend \
  --image gcr.io/YOUR_PROJECT_ID/agrismart-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_api_key_here \
  --set-env-vars ENVIRONMENT=production \
  --max-instances 10 \
  --memory 512Mi \
  --timeout 300

# Obter URL do backend
gcloud run services describe agrismart-backend \
  --platform managed \
  --region us-central1 \
  --format 'value(status.url)'
```

### Frontend

```bash
cd frontend

# Build da imagem
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/agrismart-frontend

# Deploy no Cloud Run
gcloud run deploy agrismart-frontend \
  --image gcr.io/YOUR_PROJECT_ID/agrismart-frontend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --max-instances 10 \
  --memory 256Mi

# Obter URL do frontend
gcloud run services describe agrismart-frontend \
  --platform managed \
  --region us-central1 \
  --format 'value(status.url)'
```

## 🔐 Configurar Secrets

### Opção 1: Variáveis de Ambiente

```bash
# Atualizar variáveis de ambiente do backend
gcloud run services update agrismart-backend \
  --set-env-vars GOOGLE_API_KEY=your_key_here \
  --set-env-vars CORS_ORIGINS=https://your-frontend-url.run.app \
  --region us-central1
```

### Opção 2: Secret Manager (Recomendado)

```bash
# Criar secret
echo -n "your_api_key_here" | \
  gcloud secrets create google-api-key --data-file=-

# Conceder permissão
gcloud secrets add-iam-policy-binding google-api-key \
  --member=serviceAccount:YOUR_PROJECT_NUMBER-compute@developer.gserviceaccount.com \
  --role=roles/secretmanager.secretAccessor

# Deploy com secret
gcloud run deploy agrismart-backend \
  --image gcr.io/YOUR_PROJECT_ID/agrismart-backend \
  --set-secrets=GOOGLE_API_KEY=google-api-key:latest \
  --region us-central1
```

## 🌐 Configurar CORS

Após o deploy, você precisa configurar o CORS no backend para aceitar requisições do frontend:

```bash
# Obter URL do frontend
FRONTEND_URL=$(gcloud run services describe agrismart-frontend \
  --platform managed \
  --region us-central1 \
  --format 'value(status.url)')

# Atualizar CORS
gcloud run services update agrismart-backend \
  --set-env-vars CORS_ORIGINS=$FRONTEND_URL \
  --region us-central1
```

## 🔄 Deploy Contínuo com Cloud Build

### 1. Conectar Repositório

```bash
# Conectar GitHub ao Cloud Build
gcloud alpha builds triggers create github \
  --repo-name=agrismart-brasil \
  --repo-owner=YOUR_GITHUB_USERNAME \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml
```

### 2. Push para Deploy

Agora, todo push para a branch `main` irá automaticamente:
1. Fazer build das imagens
2. Push para Container Registry
3. Deploy no Cloud Run

```bash
git add .
git commit -m "Deploy to production"
git push origin main
```

## 📊 Monitoramento

### Visualizar Logs

```bash
# Logs do backend
gcloud run services logs read agrismart-backend --region us-central1

# Logs do frontend
gcloud run services logs read agrismart-frontend --region us-central1

# Seguir logs em tempo real
gcloud run services logs tail agrismart-backend --region us-central1
```

### Métricas no Console

Acesse o [Cloud Console](https://console.cloud.google.com/run) para ver:
- Número de requisições
- Latência
- Uso de memória
- Erros

## 💰 Estimativa de Custos

Cloud Run cobra baseado em:
- Número de requisições
- Tempo de CPU utilizado
- Memória alocada

### Tier Gratuito (por mês)
- 2 milhões de requisições
- 360,000 GB-segundos de memória
- 180,000 vCPU-segundos

Para uso normal, o custo mensal estimado é de **$0 a $20** dependendo do tráfego.

## 🔧 Troubleshooting

### Erro: "Permission Denied"

```bash
# Adicionar permissão de Cloud Run Admin
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member=user:YOUR_EMAIL \
  --role=roles/run.admin
```

### Erro: "Container failed to start"

```bash
# Verificar logs de build
gcloud builds list --limit=5

# Ver detalhes do último build
gcloud builds log $(gcloud builds list --limit=1 --format='value(id)')
```

### Frontend não conecta ao Backend

1. Verifique CORS no backend
2. Confirme que as URLs estão corretas
3. Verifique se o backend está respondendo:

```bash
curl https://your-backend-url.run.app/health
```

## 🔄 Atualização

Para atualizar o serviço:

```bash
# Método 1: Re-executar deploy script
./deploy.sh

# Método 2: Build e deploy manual
cd backend
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/agrismart-backend
gcloud run deploy agrismart-backend \
  --image gcr.io/YOUR_PROJECT_ID/agrismart-backend \
  --region us-central1
```

## 🗑️ Cleanup

Para remover todos os recursos:

```bash
# Deletar serviços Cloud Run
gcloud run services delete agrismart-backend --region us-central1
gcloud run services delete agrismart-frontend --region us-central1

# Deletar imagens do Container Registry
gcloud container images delete gcr.io/YOUR_PROJECT_ID/agrismart-backend
gcloud container images delete gcr.io/YOUR_PROJECT_ID/agrismart-frontend

# Deletar secrets
gcloud secrets delete google-api-key
```

## 📞 Suporte

Se encontrar problemas:
1. Verifique os logs: `gcloud run services logs read SERVICE_NAME`
2. Consulte a [documentação do Cloud Run](https://cloud.google.com/run/docs)
3. Abra uma issue no GitHub

---

**Bom deploy! 🚀**

