from flask import Flask
import os

app = Flask('hello-gitops')

@app.route('/')
def hello():
  try:
    text = os.environ['PODTEXT']
    return f"{text}\n"
  except KeyError as err:
    print(f"Given key not found - {err}")
  
  return "Hello gitops!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
