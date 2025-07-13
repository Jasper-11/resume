#!/usr/bin/env python3
"""
Deployment script for the Flask resume website.
Supports multiple cloud platforms.
"""

import os
import subprocess
import sys

def build_project():
    """Build the Vue.js project"""
    print("🔨 Building Vue.js project...")
    try:
        subprocess.run(['npm', 'run', 'build'], check=True)
        print("✅ Build completed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Build failed!")
        sys.exit(1)

def create_procfile():
    """Create Procfile for Heroku/Railway"""
    procfile_content = """web: python app.py
"""
    with open('Procfile', 'w') as f:
        f.write(procfile_content)
    print("📄 Created Procfile")

def create_runtime_txt():
    """Create runtime.txt for Python version"""
    runtime_content = """python-3.10.11
"""
    with open('runtime.txt', 'w') as f:
        f.write(runtime_content)
    print("📄 Created runtime.txt")

def setup_for_heroku():
    """Setup for Heroku deployment"""
    print("\n🚀 Setting up for Heroku deployment...")
    create_procfile()
    create_runtime_txt()
    
    # Update app.py for production
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Replace development settings with production
    content = content.replace(
        "app.run(debug=True, host='0.0.0.0', port=5001)",
        "app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))"
    )
    
    with open('app.py', 'w') as f:
        f.write(content)
    
    print("✅ Heroku configuration complete!")
    print("\n📋 Next steps:")
    print("1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli")
    print("2. Run: heroku login")
    print("3. Run: heroku create your-app-name")
    print("4. Run: git add . && git commit -m 'Deploy resume site'")
    print("5. Run: git push heroku main")

def setup_for_railway():
    """Setup for Railway deployment"""
    print("\n🚂 Setting up for Railway deployment...")
    create_procfile()
    create_runtime_txt()
    
    # Update app.py for production
    with open('app.py', 'r') as f:
        content = f.read()
    
    content = content.replace(
        "app.run(debug=True, host='0.0.0.0', port=5001)",
        "app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))"
    )
    
    with open('app.py', 'w') as f:
        f.write(content)
    
    print("✅ Railway configuration complete!")
    print("\n📋 Next steps:")
    print("1. Go to: https://railway.app")
    print("2. Connect your GitHub repository")
    print("3. Deploy automatically!")

def setup_for_render():
    """Setup for Render deployment"""
    print("\n🎨 Setting up for Render deployment...")
    
    # Create build script
    build_script = """#!/usr/bin/env bash
npm install
npm run build
"""
    with open('build.sh', 'w') as f:
        f.write(build_script)
    
    # Create start script
    start_script = """#!/usr/bin/env bash
python app.py
"""
    with open('start.sh', 'w') as f:
        f.write(start_script)
    
    # Update app.py for production
    with open('app.py', 'r') as f:
        content = f.read()
    
    content = content.replace(
        "app.run(debug=True, host='0.0.0.0', port=5001)",
        "app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))"
    )
    
    with open('app.py', 'w') as f:
        f.write(content)
    
    print("✅ Render configuration complete!")
    print("\n📋 Next steps:")
    print("1. Go to: https://render.com")
    print("2. Create new Web Service")
    print("3. Connect your GitHub repository")
    print("4. Build Command: ./build.sh")
    print("5. Start Command: ./start.sh")

def main():
    """Main deployment function"""
    print("🌐 Resume Website Deployment")
    print("=" * 40)
    
    # Build the project first
    build_project()
    
    print("\n📋 Choose deployment platform:")
    print("1. Heroku")
    print("2. Railway")
    print("3. Render")
    print("4. Local Network (already working)")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        setup_for_heroku()
    elif choice == "2":
        setup_for_railway()
    elif choice == "3":
        setup_for_render()
    elif choice == "4":
        print("\n✅ Your site is already accessible at:")
        print("   Local: http://localhost:5001")
        print("   Network: http://192.168.0.245:5001")
        print("\n💡 To make it public, configure port forwarding on your router.")
    else:
        print("❌ Invalid choice!")

if __name__ == '__main__':
    main() 