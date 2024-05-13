from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run-server')
def run_server():
    try:
        subprocess.run(["python", "server.py"]) # Adjust command as needed
        return "Server started successfully"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) # Adjust port as needed
