#!/bin/bash

# AgriSmart Brasil - Deploy Script
# This script deploys the application to Google Cloud Run

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🌾 AgriSmart Brasil - Deploy Script${NC}"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}Error: gcloud CLI is not installed${NC}"
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if project ID is set
if [ -z "$GOOGLE_CLOUD_PROJECT" ]; then
    echo -e "${YELLOW}Please enter your Google Cloud Project ID:${NC}"
    read -r PROJECT_ID
    export GOOGLE_CLOUD_PROJECT=$PROJECT_ID
else
    PROJECT_ID=$GOOGLE_CLOUD_PROJECT
fi

echo -e "${GREEN}Using project: $PROJECT_ID${NC}"
echo ""

# Set the project
gcloud config set project "$PROJECT_ID"

# Enable required APIs
echo -e "${GREEN}Enabling required APIs...${NC}"
gcloud services enable \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    containerregistry.googleapis.com \
    artifactregistry.googleapis.com

# Build and deploy backend
echo ""
echo -e "${GREEN}Building backend...${NC}"
cd backend
gcloud builds submit --tag "gcr.io/$PROJECT_ID/agrismart-backend"

echo ""
echo -e "${GREEN}Deploying backend to Cloud Run...${NC}"
gcloud run deploy agrismart-backend \
    --image "gcr.io/$PROJECT_ID/agrismart-backend" \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --max-instances 10 \
    --memory 512Mi \
    --timeout 300

# Get backend URL
BACKEND_URL=$(gcloud run services describe agrismart-backend --platform managed --region us-central1 --format 'value(status.url)')
echo -e "${GREEN}Backend deployed at: $BACKEND_URL${NC}"

cd ..

# Build and deploy frontend
echo ""
echo -e "${GREEN}Building frontend...${NC}"
cd frontend
gcloud builds submit --tag "gcr.io/$PROJECT_ID/agrismart-frontend"

echo ""
echo -e "${GREEN}Deploying frontend to Cloud Run...${NC}"
gcloud run deploy agrismart-frontend \
    --image "gcr.io/$PROJECT_ID/agrismart-frontend" \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --max-instances 10 \
    --memory 256Mi

# Get frontend URL
FRONTEND_URL=$(gcloud run services describe agrismart-frontend --platform managed --region us-central1 --format 'value(status.url)')
echo -e "${GREEN}Frontend deployed at: $FRONTEND_URL${NC}"

cd ..

echo ""
echo -e "${GREEN}✅ Deployment completed successfully!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Update CORS_ORIGINS in backend environment variables to include: $FRONTEND_URL"
echo "2. Update frontend to use backend URL: $BACKEND_URL"
echo "3. Configure your GOOGLE_API_KEY secret in Cloud Run"
echo ""
echo -e "${GREEN}Access your application at: $FRONTEND_URL${NC}"

