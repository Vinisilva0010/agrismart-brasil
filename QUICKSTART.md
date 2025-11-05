# ⚡ Início Rápido - AgriSmart Brasil

Guia rápido para ter o AgriSmart Brasil rodando em minutos!

## 🎯 Pré-requisitos

- Python 3.11+
- Node.js 20+
- Google AI API Key ([obtenha aqui](https://makersuite.google.com/app/apikey))

## 🚀 Instalação em 5 Minutos

### 1. Clone o Repositório

```bash
git clone https://github.com/yourusername/agrismart-brasil.git
cd agrismart-brasil
```

### 2. Configure o Backend

```bash
cd backend

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
copy env.example .env  # Windows
# ou
cp env.example .env    # Linux/Mac

# Edite o .env e adicione sua GOOGLE_API_KEY
```

**Edite `.env`:**
```env
GOOGLE_API_KEY=sua_chave_aqui
CORS_ORIGINS=http://localhost:5173
```

### 3. Inicie o Backend

```bash
# Na pasta backend/
uvicorn api.main:app --reload --port 8080
```

✅ Backend rodando em: http://localhost:8080

### 4. Configure o Frontend

**Em outro terminal:**

```bash
cd frontend

# Instale dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

✅ Frontend rodando em: http://localhost:5173

## 🎮 Usando o Sistema

### Dashboard
1. Acesse http://localhost:5173
2. Veja as métricas da fazenda
3. Clique em "Gerar Briefing" para obter insights diários

### Consultar Agentes
1. Clique na aba "Consultar Agentes"
2. Digite perguntas como:
   - "Qual a melhor época para plantar milho?"
   - "Como está o clima para os próximos dias?"
   - "Preciso irrigar hoje?"
3. Receba respostas inteligentes dos agentes especializados

### Analisar Cultura
1. Clique na aba "Analisar Cultura"
2. Selecione o tipo de cultura
3. Faça upload de uma foto da planta
4. Clique em "Analisar Imagem"
5. Receba diagnóstico com recomendações

## 📡 Testando a API

### Health Check

```bash
curl http://localhost:8080/health
```

### Análise Climática

```bash
curl -X POST http://localhost:8080/api/climate/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "location": "São Paulo, Brasil",
    "climate_data": {
      "temperature": 28,
      "humidity": 65,
      "rainfall": 10,
      "wind_speed": 15
    }
  }'
```

### Previsão de Produção

```bash
curl -X POST http://localhost:8080/api/yield/predict \
  -H "Content-Type: application/json" \
  -d '{
    "crop_type": "Soja",
    "field_size": 50,
    "planting_date": "2024-10-15",
    "current_conditions": {
      "growth_stage": "Vegetativo",
      "health_status": "Bom",
      "soil_quality": "Adequado"
    }
  }'
```

## 🐳 Usando Docker (Opcional)

### Com Docker Compose

```bash
# Configure a GOOGLE_API_KEY no arquivo .env na raiz do projeto
echo "GOOGLE_API_KEY=sua_chave_aqui" > .env

# Inicie todos os serviços
docker-compose up
```

Acesse:
- Frontend: http://localhost:5173
- Backend: http://localhost:8080

### Apenas Backend

```bash
cd backend
docker build -t agrismart-backend .
docker run -p 8080:8080 --env-file .env agrismart-backend
```

### Apenas Frontend

```bash
cd frontend
docker build -t agrismart-frontend .
docker run -p 8080:8080 agrismart-frontend
```

## 🔍 Verificar se está funcionando

### Backend
- Abra http://localhost:8080/api/docs
- Você verá a documentação interativa da API
- Teste os endpoints diretamente na interface

### Frontend
- Abra http://localhost:5173
- Você verá o dashboard do AgriSmart Brasil
- Teste as 3 abas: Dashboard, Consultar Agentes, Analisar Cultura

## 🐛 Problemas Comuns

### Backend não inicia

**Erro:** `ModuleNotFoundError: No module named 'fastapi'`
```bash
# Certifique-se de estar no ambiente virtual
cd backend
source venv/bin/activate  # ou venv\Scripts\activate
pip install -r requirements.txt
```

**Erro:** `GOOGLE_API_KEY environment variable not set`
```bash
# Configure o .env com sua chave
echo "GOOGLE_API_KEY=sua_chave_aqui" >> .env
```

### Frontend não conecta ao Backend

**Erro:** `Failed to fetch` no console do navegador

1. Verifique se o backend está rodando em http://localhost:8080
2. Teste: `curl http://localhost:8080/health`
3. Verifique CORS no backend `.env`:
   ```
   CORS_ORIGINS=http://localhost:5173
   ```

### Porta já em uso

```bash
# Backend (porta 8080)
uvicorn api.main:app --reload --port 8081

# Frontend (porta 5173)
npm run dev -- --port 5174
```

## 📚 Próximos Passos

1. **Explore a API**: http://localhost:8080/api/docs
2. **Leia a documentação**: [README.md](README.md)
3. **Deploy na nuvem**: [DEPLOYMENT.md](DEPLOYMENT.md)
4. **Contribua**: [CONTRIBUTING.md](CONTRIBUTING.md)

## 🆘 Precisa de Ajuda?

- 📖 [Documentação Completa](README.md)
- 🚀 [Guia de Deploy](DEPLOYMENT.md)
- 🐛 [Abrir Issue](https://github.com/yourusername/agrismart-brasil/issues)

## 🎉 Pronto!

Você agora tem um sistema completo de agricultura inteligente rodando localmente!

**Próximos passos sugeridos:**
1. Personalize os dados da fazenda
2. Teste todos os agentes especializados
3. Faça upload de fotos reais de culturas
4. Explore as diferentes funcionalidades

---

**Bom uso! 🌾**

