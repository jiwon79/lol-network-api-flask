from flask import Flask
from flask_cors import CORS
import time
from modules.opgg import *

ORIGIN = [
    'http://lol-network.netlify.app/',
    'https://lol-network.netlify.app/',
    'http://lol-network.netlify.app',
    'https://lol-network.netlify.app',
    'http://localhost',
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:3002',
    'http://localhost:5500',
    'http://localhost:5501',
    'http://localhost:8000',
    'http://127.0.0.1',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:3001',
    'http://127.0.0.1:3002',
    'http://127.0.0.1:5500',
    'http://127.0.0.1:5501',
    'http://127.0.0.1:8000',
]

app = Flask(__name__)
cors = CORS(app, resources={
  r"*": {"origin": ORIGIN}
})

@app.route("/")
def main():
  result = {"result": '결과'}
  return result

@app.route("/userlog/<user_name>")
def get_user_log(user_name: str):
    user_log = getUserAllGameData(user_name)
    return user_log

@app.route("/friend/<user_name>")
def get_user_friend(user_name):
  user_log = getUserAllGameData(user_name)
  if (user_log == {}):
    return {"result": "no-summoner"}
  
  friend = getUserFrield(user_log)
  return friend

@app.route("/duration/<int:duration>")
def waitDuration(duration):
  for i in range(duration):
    print(i+1)
    time.sleep(1)
  return {"result" : str(duration)+' end'}


# if __name__ == "__main__":
#   app.run(debug=True)