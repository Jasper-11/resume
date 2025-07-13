# Jasper Karlen - Resume Website

A professional resume website built with Vue.js and served via Flask.

## Features

- Modern, responsive design
- Professional resume layout
- Dark theme optimized for readability
- Served via Flask backend

## Setup Instructions

### Prerequisites

- Python 3.7+
- Node.js 14+
- npm

### Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Build the Vue.js project:**
   ```bash
   npm run build
   ```

### Running the Application

**Option 1: Run with Flask (Production)**
```bash
python app.py
```
The site will be available at: http://localhost:5000

**Option 2: Development mode (Vue.js dev server)**
```bash
npm run dev
```
The development server will be available at: http://localhost:5173

## Deployment

### Local Development
- Use `npm run dev` for Vue.js development with hot reload
- Use `python app.py` for Flask production server

### Production Deployment
1. Build the Vue.js project: `npm run build`
2. Start the Flask server: `python app.py`
3. The Flask app will automatically serve the built files from the `dist` directory

## Project Structure

```
├── app.py              # Flask backend server
├── requirements.txt    # Python dependencies
├── package.json       # Node.js dependencies
├── index.html         # Main HTML template
├── src/
│   ├── App.vue        # Main Vue component
│   └── main.js        # Vue app entry point
└── dist/              # Built files (generated after build)
```

## Customization

- Edit `src/App.vue` to modify the resume content
- Update styles in the `<style>` section of `App.vue`
- Modify `app.py` for additional Flask routes or API endpoints

## Technologies Used

- **Frontend:** Vue.js 3, Vite
- **Backend:** Flask (Python)
- **Styling:** CSS with dark theme
- **Build Tool:** Vite 