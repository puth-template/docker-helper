# MinIO Dockerfile
# Version will be set by version-manager script
ARG MINIO_VERSION=latest
FROM minio/minio:${MINIO_VERSION}

# Set environment variables
ENV MINIO_ROOT_USER=admin
ENV MINIO_ROOT_PASSWORD=abc123456

# Create data directory
RUN mkdir -p /data

# Expose ports
EXPOSE 9000 9001

# Default command
CMD ["server", "/data", "--console-address", ":9001"]
