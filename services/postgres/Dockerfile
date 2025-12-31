# PostgreSQL Dockerfile
# Version will be set by version-manager script
ARG POSTGRES_VERSION=16
FROM postgres:${POSTGRES_VERSION}

# Set environment variables
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=abc123
ENV POSTGRES_DB=kjc_dev

# Create data directory
RUN mkdir -p /var/lib/postgresql/data

# Expose port
EXPOSE 5432

# Default command
CMD ["postgres"]
