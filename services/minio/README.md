# MinIO Service

## Mô tả
MinIO S3-compatible object storage service

## Cấu hình
- **API Port**: 9000
- **Console Port**: 9001
- **Username**: admin
- **Password**: abc123456
- **Container name**: minio

## Cách sử dụng

### Chạy riêng lẻ
```bash
cd services/minio
docker-compose up -d
```

### Build từ Dockerfile
```bash
cd services/minio
docker build -t minio-custom .
docker-compose up -d
```

### Truy cập
- **Web Console**: http://localhost:9001
- **API Endpoint**: http://localhost:9000

## 🔄 Version Management

### Xem các version có sẵn
```bash
scripts/version-manager.bat list -s minio
```

### Thay đổi version
```bash
# Đặt version mới
scripts/version-manager.bat set -s minio -v RELEASE.2024-01-16T16-07-38Z

# Build với version mới
scripts/version-manager.bat build -s minio
```

### Available Versions
- **RELEASE.2023-12-20T10-07-38Z** - MinIO December 2023 (Stable)
- **RELEASE.2024-01-16T16-07-38Z** - MinIO January 2024 (Stable)
- **latest** - MinIO Latest (Current)
- **edge** - MinIO Edge (Experimental)

## Files
- `docker-compose.yml` - Cấu hình Docker Compose
- `Dockerfile` - Dockerfile để build custom image
- `versions/version.yml` - Cấu hình version và features
