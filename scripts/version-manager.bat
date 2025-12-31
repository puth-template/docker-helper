@echo off
REM Version Manager Script for Windows
REM Usage: version-manager.bat [action] [options]

if "%1"=="" (
    echo Usage: version-manager.bat [list^|set^|build^|current] [options]
    echo.
    echo Actions:
    echo   list     - List available versions for a service
    echo   set      - Set current version for a service
    echo   build    - Build Docker image for a service
    echo   current  - Show current version for a service
    echo.
    echo Options:
    echo   -s, --service  Service name (mongo, postgres, redis, minio)
    echo   -v, --version  Version to set or build
    echo.
    echo Examples:
    echo   version-manager.bat list -s mongo
    echo   version-manager.bat set -s mongo -v 8.0
    echo   version-manager.bat build -s postgres -v 15
    echo   version-manager.bat current -s redis
    goto :eof
)

python scripts/version-manager.py %*
