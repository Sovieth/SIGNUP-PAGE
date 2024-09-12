from app import create_app
import os
from flask import Flask

app = create_app()

if __name__ == "_main_":
    app.run(debug=True, host="0.0.0.0")
