# Docker Compose Services

## 📁 Cấu trúc thư mục

```
doker-compose/
├── docker-compose.yml          # File chính với include và cấu hình chung
├── scripts/                    # Scripts quản lý version
│   ├── version-manager.py     # Python script quản lý version
│   └── version-manager.bat    # Windows batch script
├── services/                   # Thư mục chứa các service riêng lẻ
│   ├── mongo/                 # MongoDB service
│   │   ├── docker-compose.yml
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── versions/          # Thư mục quản lý version
│   │       └── version.yml    # Cấu hình version
│   ├── postgres/              # PostgreSQL service
│   │   ├── docker-compose.yml
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── versions/
│   │       └── version.yml
│   ├── redis/                 # Redis service
│   │   ├── docker-compose.yml
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── versions/
│   │       └── version.yml
│   ├── minio/                 # MinIO service
│   │   ├── docker-compose.yml
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── versions/
│   │       └── version.yml
│   └── postfix/               # Postfix service
│       ├── docker-compose.yml
│       ├── Dockerfile
│       ├── README.md
│       ├── config/            # Postfix configuration
│       │   ├── main.cf
│       │   └── master.cf
│       └── versions/
│           └── version.yml
└── setting.md
```

## 🚀 Cách sử dụng

### Chạy tất cả services
```bash
docker-compose up -d
```

### Chạy riêng lẻ từng service
```bash
# MongoDB
cd services/mongo
docker-compose up -d

# PostgreSQL
cd services/postgres
docker-compose up -d

# Redis
cd services/redis
docker-compose up -d

# MinIO
cd services/minio
docker-compose up -d

# Postfix
cd services/postfix
docker-compose up -d
```

### Build custom images
```bash
# Build tất cả
docker-compose build

# Build riêng lẻ
cd services/mongo
docker-compose build
```

## 🔄 Quản lý Version

### Xem các version có sẵn
```bash
# Xem tất cả services
scripts/version-manager.bat list

# Xem version của một service cụ thể
scripts/version-manager.bat list -s mongo
```

### Thay đổi version
```bash
# Đặt version mới cho service
scripts/version-manager.bat set -s mongo -v 8.0
scripts/version-manager.bat set -s postgres -v 15
```

### Build với version cụ thể
```bash
# Build với version hiện tại
scripts/version-manager.bat build -s mongo

# Build với version cụ thể
scripts/version-manager.bat build -s mongo -v 8.0
```

### Xem version hiện tại
```bash
scripts/version-manager.bat current -s mongo
```

## 🔧 Services

| Service | Port | Description |
|---------|------|-------------|
| MongoDB | 27017 | NoSQL Database |
| PostgreSQL | 5432 | SQL Database |
| Redis | 6379 | Cache & Session Store |
| MinIO | 9000/9001 | S3-compatible Object Storage |
| Postfix | 25/587/465 | Mail Server (SMTP) |

## 📝 Lưu ý

- Mỗi service có thể chạy độc lập
- Có thể customize Dockerfile cho từng service
- Tất cả services đều sử dụng chung network `app-network`
- Volumes được quản lý tập trung trong file chính
