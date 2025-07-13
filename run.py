#!/usr/bin/env python3
"""
Simple runner script for the Flask resume application.
Handles building and serving the Vue.js application.
"""

import os
import sys
import subprocess
from app import app

def build_vue_project():
    """Build the Vue.js project if dist directory doesn't exist"""
    if not os.path.exists('dist'):
        print("Building Vue.js project...")
        try:
            subprocess.run(['npm', 'run', 'build'], check=True)
            print("✅ Vue.js project built successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to build Vue.js project. Make sure you have Node.js and npm installed.")
            sys.exit(1)
    else:
        print("✅ Vue.js project already built.")

def main():
    """Main function to run the Flask application"""
    print("🚀 Starting Jasper Karlen Resume Website")
    print("=" * 50)
    
    # Check if Node.js dependencies are installed
    if not os.path.exists('node_modules'):
        print("Installing Node.js dependencies...")
        try:
            subprocess.run(['npm', 'install'], check=True)
            print("✅ Node.js dependencies installed!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install Node.js dependencies.")
            sys.exit(1)
    
    # Build Vue.js project
    build_vue_project()
    
    print("\n🌐 Starting Flask server...")
    print("📍 Resume site will be available at: http://localhost:5001")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5001)

if __name__ == '__main__':
    main() 