# Script para corrigir CORS e fazer redeploy
# AgriSmart Brasil

Write-Host "🔧 Corrigindo CORS e fazendo redeploy..." -ForegroundColor Green
Write-Host ""

# Navegar para backend
Set-Location -Path "C:\Users\vnspo\OneDrive\Documentos\agrismart-brasil\backend"

Write-Host "📦 Fazendo deploy do backend com CORS corrigido..." -ForegroundColor Yellow

# Deploy do backend
gcloud run deploy agrismart-backend `
  --source . `
  --region southamerica-east1 `
  --allow-unauthenticated `
  --platform managed `
  --set-env-vars GOOGLE_API_KEY=AIzaSyCnBDhU-QUxZCFrsdfcosWDYYm_FDCmTZQ `
  --timeout 300 `
  --memory 512Mi

Write-Host ""
Write-Host "✅ Backend redesployado!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 URLs:" -ForegroundColor Cyan
Write-Host "Frontend: https://agrismart-frontend-305905232437.southamerica-east1.run.app"
Write-Host "Backend:  https://agrismart-backend-305905232437.southamerica-east1.run.app"
Write-Host ""
Write-Host "⏰ Aguarde 1-2 minutos e teste o frontend novamente!" -ForegroundColor Yellow
Write-Host "Force refresh: Ctrl+Shift+R" -ForegroundColor Yellow

