from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configure static folder for built Vue.js files
app.static_folder = 'dist'
app.static_url_path = ''

@app.route('/')
def index():
    """Serve the main resume page"""
    return send_from_directory('dist', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files from the dist directory"""
    return send_from_directory('dist', path)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors by serving the main page (for SPA routing)"""
    return send_from_directory('dist', 'index.html')

if __name__ == '__main__':
    # Check if dist directory exists, if not build the project
    if not os.path.exists('dist'):
        print("Building Vue.js project...")
        os.system('npm run build')
    
    print("Starting Flask server...")
    print("Resume site available at: http://localhost:5001")
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5001))) 