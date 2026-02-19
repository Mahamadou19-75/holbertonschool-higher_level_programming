#!/usr/bin/python3
from task_04_flask import app

if __name__ == "__main__":
    # Exécuter le serveur Flask sur le port 5000
    app.run(host="0.0.0.0", port=5000)

