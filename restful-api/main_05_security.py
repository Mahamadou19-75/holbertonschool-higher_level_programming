#!/usr/bin/python3
from task_05_basic_security import app

if __name__ == "__main__":
    # Lancer le serveur Flask sur le port 5000
    app.run(host="0.0.0.0", port=5000)

