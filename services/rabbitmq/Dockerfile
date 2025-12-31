# RabbitMQ Dockerfile
# Version will be set by version-manager script
ARG RABBITMQ_VERSION=3.13-management
FROM rabbitmq:${RABBITMQ_VERSION}

# Set environment variables
ENV RABBITMQ_DEFAULT_USER=admin
ENV RABBITMQ_DEFAULT_PASS=admin123
ENV RABBITMQ_DEFAULT_VHOST=/

# Enable management plugin
RUN rabbitmq-plugins enable rabbitmq_management

# Expose ports
EXPOSE 5672 15672

# Default command
CMD ["rabbitmq-server"]


