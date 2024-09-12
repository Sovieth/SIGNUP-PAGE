from app import create_app
import os

app = create_app()

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5000)