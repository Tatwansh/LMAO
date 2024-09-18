from flask import Flask
from config import Config


# Create a flask instance
app = Flask(__name__)
app.config.from_object(Config)
