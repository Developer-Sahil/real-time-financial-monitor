# Real-Time Financial Data Monitor (RFD Monitor)

This project is a full-stack financial data dashboard that fetches, visualizes, and alerts users based on asset price movements.

## 🌐 Live Demo
[View the Live Project](https://thunderous-figolla-0fe5f4.netlify.app/)

## Files Included

- `rfd-monitor.html`: The frontend application. It's a single, self-contained file with HTML, Tailwind CSS (via CDN), and JavaScript. It simulates a backend for immediate use.
- `main.py`: The Python backend server built with FastAPI. This provides the API endpoints that the frontend would call in a real deployment.
- `requirements.txt`: A file listing the Python dependencies for the backend.
- `README.md`: This file.

## How to Run

### Option 1: Frontend Only (Simulated Backend)

1.  Simply open the `rfd-monitor.html` file in any modern web browser (like Chrome, Firefox, or Edge).
2.  The dashboard will work out-of-the-box using the simulated data generator in the JavaScript code.

### Option 2: Full Stack (Frontend + Python Backend)

1.  **Set up the Backend:**
    * Make sure you have Python 3.7+ installed.
    * **Install the required libraries using `requirements.txt`:**
        ```bash
        pip install -r requirements.txt
        ```
    * Navigate to the project directory in your terminal.
    * Run the backend server:
        ```bash
        uvicorn main:app --reload
        ```
    * The API will be running at `http://127.0.0.1:8000`.

2.  **Connect the Frontend:**
    * Open the `rfd-monitor.html` file in a code editor.
    * Find the `// --- MOCK BACKEND API ---` section in the `<script>` tag.
    * Replace the `fetchMockPrice` function with a real `fetch` call to your running backend.

3.  **View the Application:**
    * Open `rfd-monitor.html` in your web browser. It will now be fetching live (simulated) data from your Python backend.
