# Build stage
FROM node:20-alpine as build

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install missing dependencies explicitly first
RUN npm install --save-dev vite-plugin-markdown gh-pages && \
    npm install react-router-dom react-markdown rehype-raw rehype-sanitize remark-gfm

# Install regular dependencies
RUN npm install

# Copy project files
COPY . .

# Build the app
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built files to nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx config if you have custom configuration
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]