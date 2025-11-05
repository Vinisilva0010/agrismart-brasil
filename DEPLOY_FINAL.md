# 🚀 DEPLOY FINAL - AgriSmart Brasil

## ⚠️ PROBLEMA ATUAL
CORS não está funcionando em produção - backend precisa ser redesployado com código corrigido.

---

## ✅ SOLUÇÃO: Execute estes comandos

### 1️⃣ Abra PowerShell ou CMD onde o `gcloud` funciona

### 2️⃣ Navegue para o backend:
```cmd
cd C:\Users\vnspo\OneDrive\Documentos\agrismart-brasil\backend
```

### 3️⃣ Execute o deploy do backend:
```cmd
gcloud run deploy agrismart-backend --source . --region southamerica-east1 --allow-unauthenticated --platform managed --set-env-vars GOOGLE_API_KEY=AIzaSyCnBDhU-QUxZCFrsdfcosWDYYm_FDCmTZQ --timeout 300 --memory 512Mi
```

**Aguarde o deploy terminar (2-5 minutos)**

### 4️⃣ Verifique se funcionou:
```cmd
curl https://agrismart-backend-305905232437.southamerica-east1.run.app/health
```

Deve retornar: `{"status":"healthy","service":"agrismart-brasil"}`

### 5️⃣ Teste o frontend:
👉 **https://agrismart-frontend-305905232437.southamerica-east1.run.app**

**Force refresh**: Ctrl+Shift+R (Windows) ou Cmd+Shift+R (Mac)

---

## 🌐 URLs FINAIS (Após Deploy)

- **Frontend**: https://agrismart-frontend-305905232437.southamerica-east1.run.app
- **Backend**: https://agrismart-backend-305905232437.southamerica-east1.run.app
- **API Docs**: https://agrismart-backend-305905232437.southamerica-east1.run.app/api/docs

---

## 🔍 VERIFICAÇÃO

Após o deploy, teste:

1. **Abra o frontend** no navegador
2. **Aba "Consultar Agentes"**
3. **Digite**: "Qual a melhor época para plantar soja?"
4. **Deve funcionar sem erro CORS!** ✅

---

## ⚡ SE NÃO FUNCIONAR

### Opção 1: Cloud Shell (Mais Fácil)

1. Acesse: https://console.cloud.google.com/run?project=305905232437
2. Clique no ícone **Cloud Shell** (terminal no canto superior direito)
3. Execute:

```bash
git clone https://github.com/Vinisilva0010/agrismart-brasil.git
cd agrismart-brasil/backend

gcloud run deploy agrismart-backend \
  --source . \
  --region southamerica-east1 \
  --allow-unauthenticated \
  --platform managed \
  --set-env-vars GOOGLE_API_KEY=AIzaSyCnBDhU-QUxZCFrsdfcosWDYYm_FDCmTZQ \
  --timeout 300 \
  --memory 512Mi
```

### Opção 2: Verificar Logs

```cmd
gcloud run services logs read agrismart-backend --region southamerica-east1 --limit 50
```

---

**Execute o deploy e me avise quando terminar!** 🚀


