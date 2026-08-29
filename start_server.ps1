$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

try {
    docker info *> $null
}
catch {
    Write-Host 'Docker Desktop is not running. Start Docker Desktop, then run this script again.' -ForegroundColor Yellow
    exit 1
}

if ($LASTEXITCODE -ne 0) {
    Write-Host 'Docker Desktop is not running. Start Docker Desktop, then run this script again.' -ForegroundColor Yellow
    exit 1
}

docker compose -f docker-compose.yml up -d --build
docker compose -f docker-compose.yml exec web python manage.py migrate

Write-Host 'Server is running at http://localhost:8000/' -ForegroundColor Green