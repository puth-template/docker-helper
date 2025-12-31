# MongoDB Service

## Mô tả
MongoDB database service với phiên bản 7.0

## Cấu hình
- **Port**: 27017
- **Username**: root
- **Password**: abc123
- **Container name**: mongo

## Cách sử dụng

### Chạy riêng lẻ
```bash
cd services/mongo
docker-compose up -d
```

### Build từ Dockerfile
```bash
cd services/mongo
docker build -t mongo-custom .
docker-compose up -d
```

### Kết nối
```bash
mongosh mongodb://root:abc123@localhost:27017
```

## 🔄 Version Management

### Xem các version có sẵn
```bash
scripts/version-manager.bat list -s mongo
```

### Thay đổi version
```bash
# Đặt version mới
scripts/version-manager.bat set -s mongo -v 8.0

# Build với version mới
scripts/version-manager.bat build -s mongo
```

### Available Versions
- **6.0** - MongoDB 6.0 (LTS)
- **7.0** - MongoDB 7.0 (Current)
- **8.0** - MongoDB 8.0 (Experimental)

## Files
- `docker-compose.yml` - Cấu hình Docker Compose
- `Dockerfile` - Dockerfile để build custom image
- `versions/version.yml` - Cấu hình version và features
