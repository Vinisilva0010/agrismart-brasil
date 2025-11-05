# Build stage
FROM node:20-alpine as build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build args para variáveis de ambiente do Vite
ARG VITE_BACKEND_URL=https://agrismart-backend-305905232437.southamerica-east1.run.app
ARG VITE_ENV=production

# Definir as variáveis de ambiente para o build
ENV VITE_BACKEND_URL=${VITE_BACKEND_URL}
ENV VITE_ENV=${VITE_ENV}

# Fix permissions for node_modules binaries
RUN chmod -R +x node_modules/.bin

# Build the app
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built assets from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
