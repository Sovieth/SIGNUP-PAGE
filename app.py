from app import create_app
import os
from flask import Flask

app = create_app()

if __name__ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)