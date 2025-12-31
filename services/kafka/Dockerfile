# Kafka Dockerfile with KRaft mode (no Zookeeper)
# Version will be set by version-manager script
ARG KAFKA_VERSION=3.7.0
FROM apache/kafka:${KAFKA_VERSION}

# Switch to root to copy entrypoint script
USER root

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set working directory
WORKDIR /opt/kafka

# Expose ports
EXPOSE 9092 9093 9094 9095

# Use custom entrypoint
ENTRYPOINT ["/entrypoint.sh"]
