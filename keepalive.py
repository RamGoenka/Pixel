#THIS FILE IS USED TO KEEP THE BOT ALIVE (ONLINE) FOR 24/7
from flask import Flask
from threading import Thread 

app = Flask('')

@app.route('/')
def home():
  return "Bot Status: Online."

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    
