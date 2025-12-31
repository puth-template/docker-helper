# PostgreSQL Service

## Mô tả
PostgreSQL database service với phiên bản 16

## Cấu hình
- **Port**: 5432
- **Username**: admin
- **Password**: abc123
- **Database**: kjc_dev
- **Container name**: postgres

## Cách sử dụng

### Chạy riêng lẻ
```bash
cd services/postgres
docker-compose up -d
```

### Build từ Dockerfile
```bash
cd services/postgres
docker build -t postgres-custom .
docker-compose up -d
```

### Kết nối
```bash
psql -h localhost -p 5432 -U admin -d kjc_dev
```

## 🔄 Version Management

### Xem các version có sẵn
```bash
scripts/version-manager.bat list -s postgres
```

### Thay đổi version
```bash
# Đặt version mới
scripts/version-manager.bat set -s postgres -v 15

# Build với version mới
scripts/version-manager.bat build -s postgres
```

### Available Versions
- **14** - PostgreSQL 14 (LTS)
- **15** - PostgreSQL 15 (Stable)
- **16** - PostgreSQL 16 (Current)
- **17** - PostgreSQL 17 (Experimental)

## Files
- `docker-compose.yml` - Cấu hình Docker Compose
- `Dockerfile` - Dockerfile để build custom image
- `versions/version.yml` - Cấu hình version và features
