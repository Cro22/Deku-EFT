#!/bin/sh
set -e

# 1. Create tables
echo "⏳ Creating database tables..."
python - << 'EOF'
from app.db.connection import engine
from app.models import Base
Base.metadata.create_all(bind=engine)
EOF

# 2. Seed initial ETFs
echo "⏳ Seeding ETF data..."
python app/seed/etfs_seed.py

# 3. Finally, launch the main process
echo "🚀 Starting application..."
exec python app/main.py
