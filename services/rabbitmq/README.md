# RabbitMQ Service

## Mô tả
RabbitMQ message broker service với Management UI

## Cấu hình
- **AMQP Port**: 5672
- **Management UI Port**: 15672
- **Username**: admin
- **Password**: admin123
- **Container name**: rabbitmq
- **Default VHost**: /

## Cách sử dụng

### Chạy riêng lẻ
```bash
cd services/rabbitmq
docker-compose up -d
```

### Build từ Dockerfile
```bash
cd services/rabbitmq
docker build -t rabbitmq-custom .
docker-compose up -d
```

### Truy cập Management UI
- **URL**: http://localhost:15672
- **Username**: admin
- **Password**: admin123

### Kết nối từ ứng dụng
```javascript
// Node.js example
const amqp = require('amqplib');

const connection = await amqp.connect('amqp://admin:admin123@localhost:5672/');
const channel = await connection.createChannel();
```

```python
# Python example
import pika

connection = pika.BlockingConnection(
    pika.URLParameters('amqp://admin:admin123@localhost:5672/')
)
channel = connection.channel()
```

## 🔄 Version Management

### Xem các version có sẵn
```bash
scripts/version-manager.bat list -s rabbitmq
```

### Thay đổi version
```bash
# Đặt version mới
scripts/version-manager.bat set -s rabbitmq -v 3.14-management

# Build với version mới
scripts/version-manager.bat build -s rabbitmq
```

### Available Versions
- **3.12-management** - RabbitMQ 3.12 with Management UI (Stable)
- **3.13-management** - RabbitMQ 3.13 with Management UI (Current)
- **3.13** - RabbitMQ 3.13 without Management UI (Lightweight)
- **3.14-management** - RabbitMQ 3.14 with Management UI (Latest)

## Environment Variables
- `RABBITMQ_DEFAULT_USER` - Default username (default: admin)
- `RABBITMQ_DEFAULT_PASS` - Default password (default: admin123)
- `RABBITMQ_DEFAULT_VHOST` - Default virtual host (default: /)

## Files
- `docker-compose.yml` - Cấu hình Docker Compose
- `Dockerfile` - Dockerfile để build custom image
- `versions/version.yml` - Cấu hình version và features
- `env.example` - Template cho environment variables


