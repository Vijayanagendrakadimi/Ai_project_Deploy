from flask import Flask

app = Flask(__name__)

# Configuration settings can be added here
app.config['SECRET_KEY'] = 'your_secret_key'