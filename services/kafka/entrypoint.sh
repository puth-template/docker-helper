#!/bin/bash
set -e

# Format storage if not already formatted
if [ ! -f /tmp/kraft-combined-logs/meta.properties ]; then
  echo "Formatting Kafka storage for KRaft mode..."
  KAFKA_CLUSTER_ID=$(/opt/kafka/bin/kafka-storage.sh random-uuid)
  /opt/kafka/bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c /opt/kafka/config/kraft/server.properties
  echo "Kafka storage formatted with cluster ID: $KAFKA_CLUSTER_ID"
fi

# Start Kafka server
exec /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/kraft/server.properties
