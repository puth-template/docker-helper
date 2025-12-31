# Redis Service

## Mô tả
Redis cache service với phiên bản 7.2

## Cấu hình
- **Port**: 6379
- **Persistence**: AOF (Append Only File)
- **Container name**: redis

## Cách sử dụng

### Chạy riêng lẻ
```bash
cd services/redis
docker-compose up -d
```

### Build từ Dockerfile
```bash
cd services/redis
docker build -t redis-custom .
docker-compose up -d
```

### Kết nối
```bash
redis-cli -h localhost -p 6379
```

## 🔄 Version Management

### Xem các version có sẵn
```bash
scripts/version-manager.bat list -s redis
```

### Thay đổi version
```bash
# Đặt version mới
scripts/version-manager.bat set -s redis -v 8.0

# Build với version mới
scripts/version-manager.bat build -s redis
```

### Available Versions
- **6.2** - Redis 6.2 (LTS)
- **7.0** - Redis 7.0 (Stable)
- **7.2** - Redis 7.2 (Current)
- **8.0** - Redis 8.0 (Experimental)

## Files
- `docker-compose.yml` - Cấu hình Docker Compose
- `Dockerfile` - Dockerfile để build custom image
- `versions/version.yml` - Cấu hình version và features
