# Redis Dockerfile
# Version will be set by version-manager script
ARG REDIS_VERSION=7.2
FROM redis:${REDIS_VERSION}

# Create data directory
RUN mkdir -p /data

# Expose port
EXPOSE 6379

# Default command with persistence
CMD ["redis-server", "--appendonly", "yes"]
