# Kafka Service (KRaft Mode - No Zookeeper)

## Mô tả
Apache Kafka message broker service sử dụng KRaft mode (không cần Zookeeper). Đây là phiên bản mới nhất của Kafka với kiến trúc đơn giản hơn và hiệu suất tốt hơn.

## Cấu hình
- **Broker Port**: 9092
- **Controller Port**: 9093 (KRaft)
- **Inter-broker Port**: 9094
- **Kafka UI Port**: 8080 (Web Interface)
- **Container name**: kafka, kafka-ui
- **Mode**: KRaft (không cần Zookeeper)

## Cách sử dụng

### Chạy riêng lẻ
```bash
cd services/kafka
docker-compose up -d
```

### Build từ Dockerfile
```bash
cd services/kafka
docker build -t kafka-custom .
docker-compose up -d
```

### Truy cập Kafka UI (Web Interface)
Sau khi chạy `docker-compose up -d`, mở trình duyệt:
- **URL**: http://localhost:8080
- **Features**:
  - Xem danh sách topics
  - Xem messages trong topics
  - Tạo/xóa topics
  - Xem consumer groups
  - Xem broker information
  - Browse messages theo partition
  - Search messages

### Kiểm tra trạng thái
```bash
docker logs kafka
docker logs kafka-ui
```

### Tạo topic
```bash
docker exec -it kafka kafka-topics.sh --create \
  --topic test-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

### Liệt kê topics
```bash
docker exec -it kafka kafka-topics.sh --list \
  --bootstrap-server localhost:9092
```

### Gửi message (Producer)
```bash
docker exec -it kafka kafka-console-producer.sh \
  --topic test-topic \
  --bootstrap-server localhost:9092
```

### Nhận message (Consumer)
```bash
docker exec -it kafka kafka-console-consumer.sh \
  --topic test-topic \
  --from-beginning \
  --bootstrap-server localhost:9092
```

## Kết nối từ ứng dụng

### Node.js
```javascript
const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: ['localhost:9092']
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: 'test-group' });

// Producer
await producer.connect();
await producer.send({
  topic: 'test-topic',
  messages: [{ value: 'Hello Kafka' }]
});

// Consumer
await consumer.connect();
await consumer.subscribe({ topic: 'test-topic' });
await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    console.log({
      value: message.value.toString(),
    });
  },
});
```

### Python
```python
from kafka import KafkaProducer, KafkaConsumer

# Producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('test-topic', b'Hello Kafka')
producer.close()

# Consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest'
)
for message in consumer:
    print(message.value)
```

### Java
```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

KafkaProducer<String, String> producer = new KafkaProducer<>(props);
ProducerRecord<String, String> record = new ProducerRecord<>("test-topic", "Hello Kafka");
producer.send(record);
producer.close();
```

## 🔄 Version Management

### Xem các version có sẵn
```bash
scripts/version-manager.bat list -s kafka
```

### Thay đổi version
```bash
# Đặt version mới
scripts/version-manager.bat set -s kafka -v 3.7.1

# Build với version mới
scripts/version-manager.bat build -s kafka
```

### Available Versions
- **3.6.0** - Kafka 3.6.0 with KRaft mode (Stable)
- **3.6.1** - Kafka 3.6.1 with KRaft mode (Stable)
- **3.6.2** - Kafka 3.6.2 with KRaft mode (Stable)
- **3.7.0** - Kafka 3.7.0 with KRaft mode (Current - Latest stable)
- **3.7.1** - Kafka 3.7.1 with KRaft mode (Latest)

## Environment Variables
- `KAFKA_NODE_ID` - Node ID cho KRaft cluster (default: 1)
- `KAFKA_PROCESS_ROLES` - Roles của node: broker,controller (default: broker,controller)
- `KAFKA_CONTROLLER_QUORUM_VOTERS` - Controller quorum voters (default: 1@kafka:9093)
- `KAFKA_LISTENERS` - Listeners configuration
- `KAFKA_ADVERTISED_LISTENERS` - Advertised listeners
- `KAFKA_AUTO_CREATE_TOPICS_ENABLE` - Tự động tạo topics (default: true)

## KRaft Mode vs Zookeeper

### Ưu điểm của KRaft mode:
- ✅ **Không cần Zookeeper** - Đơn giản hóa deployment
- ✅ **Hiệu suất tốt hơn** - Giảm độ trễ và tăng throughput
- ✅ **Dễ scale hơn** - Quản lý metadata hiệu quả hơn
- ✅ **Khởi động nhanh hơn** - Không cần chờ Zookeeper
- ✅ **Tài nguyên ít hơn** - Không cần chạy Zookeeper riêng

### Lưu ý:
- KRaft mode đã production-ready từ Kafka 3.3.0+
- Các phiên bản từ 3.6.0+ đã được tối ưu cho KRaft mode
- Migration từ Zookeeper sang KRaft có thể thực hiện nhưng cần planning

## Files
- `docker-compose.yml` - Cấu hình Docker Compose
- `Dockerfile` - Dockerfile để build custom image
- `versions/version.yml` - Cấu hình version và features

## Troubleshooting

### Kiểm tra logs
```bash
docker logs kafka
```

### Kiểm tra health
```bash
docker exec -it kafka kafka-broker-api-versions --bootstrap-server localhost:9092
```

### Xóa dữ liệu và khởi động lại
```bash
docker-compose down -v
docker-compose up -d
```
