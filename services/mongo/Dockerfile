# MongoDB Dockerfile
# Version will be set by version-manager script
ARG MONGO_VERSION=7.0
FROM mongo:${MONGO_VERSION}

# Set environment variables
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=abc123

# Create data directory
RUN mkdir -p /data/db

# Expose port
EXPOSE 27017

# Default command
CMD ["mongod"]
