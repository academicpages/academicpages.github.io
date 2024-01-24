# Update the arg in docker-compose.yml or devcontainer.json to switch arg versions
ARG NODE_VERSION=18

# main image
FROM mcr.microsoft.com/devcontainers/javascript-node:${NODE_VERSION}

# Update the arg in docker-compose.yml or devcontainer.json to switch arg versions
ARG GO_VERSION=latest
ARG HUGO_VERSION=latest

# Download necessary tools
RUN apt-get update && apt-get install -y \
    ca-certificates openssl git curl && \
    rm -rf /var/lib/apt/lists/* && \
    # set architecture
    case $(uname -m) in \
    aarch64) \
    export ARCH=arm64 ;; \
    *) \
    export ARCH=amd64 ;; \
    esac && \
    # install Hugo
    wget -O hugo_extended_${HUGO_VERSION}.tar.gz https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${ARCH}.tar.gz && \
    tar xf hugo_extended_${HUGO_VERSION}.tar.gz && \
    mv hugo /usr/bin/hugo && \
    rm hugo_extended_${HUGO_VERSION}.tar.gz && \
    # install Go
    wget -O go${GO_VERSION}.linux-${ARCH}.tar.gz https://dl.google.com/go/go${GO_VERSION}.linux-${ARCH}.tar.gz && \
    tar -C /usr/local -xzf go${GO_VERSION}.linux-${ARCH}.tar.gz && \
    rm go${GO_VERSION}.linux-${ARCH}.tar.gz

# Export Go path
ENV PATH=$PATH:/usr/local/go/bin