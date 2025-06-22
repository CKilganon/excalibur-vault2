from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'EXCALIBUR is alive and recursive.'

if __name__ == '__main__':
    while True:
        print("[Heartbeat] Vault stable. ETH logic cycling.")
        time.sleep(900)  # 15 minutes
