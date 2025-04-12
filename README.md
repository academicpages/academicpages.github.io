Here's a comprehensive README.md file for your academic site project:

```markdown
# Academic Portfolio Site

A personal academic portfolio website built with React, Vite, and deployed on GitHub Pages.

## Prerequisites

- Git
- Node.js (v20.x recommended)
- npm

## Setup Instructions

### Installing NVM

Node Version Manager (NVM) allows you to easily install and switch between Node.js versions.

#### Mac/Linux

```bash
# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Add NVM to your shell profile (.zshrc, .bash_profile, etc.)
echo 'export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"' >> ~/.zshrc

# Apply changes 
source ~/.zshrc
```

#### Verify Installation

```bash
nvm --version
```

### Using Node.js v20

```bash
# Install Node.js v20
nvm install 20

# Use Node.js v20
nvm use 20

# Verify version
node -v
# Should output v20.x.x
```

### Installing Dependencies

```bash
npm install
```

## Development

### Local Development

```bash
npm run dev
```

Access the site at [http://localhost:5173](http://localhost:5173)

### Using Docker

```bash
docker compose up dev
```

## Deployment

### Deploying to GitHub Pages

```bash
# Make sure you're on Node.js v20
nvm use 20

# Build and deploy
npm run deploy
```

The deployment script will:
1. Build the project (`npm run build`)
2. Push the built files to the `gh-pages` branch

### Deployment Troubleshooting

If you encounter Node.js version issues:

```bash
# Check if you're using the correct Node version
node -v

# If not v20.x.x, switch to it
nvm use 20
```

If you prefer using Docker for deployment:

```bash
docker compose run --rm dev sh -c "npm install && npm run build && npm run deploy"
```

## Project Structure

- `/public/content/` - Markdown content files
- `/src/components/` - React components
- `/src/pages/` - Page components
- `/src/utils/` - Utility functions
```