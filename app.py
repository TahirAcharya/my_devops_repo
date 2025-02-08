from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Modified text in title</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 200px; }
            h1 { color: #3FCF; }
            button { padding: 10px 20px; font-size: 28px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Welcome to Devops</h1>
        <button onclick="alert('Button Clicked!')">Click Me</button>
    </body>
    </html>
    '''

# Run the app with port and debug mode enabled
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Listens on all IPs (useful for external access)
