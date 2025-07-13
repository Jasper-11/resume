#!/usr/bin/env bash
# Ensure dist directory exists
if [ ! -d "dist" ]; then
    echo "Building Vue.js project..."
    npm run build
fi
python app.py 