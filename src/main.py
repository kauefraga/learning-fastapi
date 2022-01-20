import requests, os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def Hello():
  return {'Hello': 'world'}

@app.get('/hi')
def Hi():
  times = int(os.environ.get('TIMES', 3))
  return {'Message': 'Hi! '*times}

@app.get('/teapot', response_class=HTMLResponse)
def Teapot():
  data = requests.get('http://httpbin.org/status/418').text
  return '<pre>'+data+'</pre>'

@app.get('db', response_class=HTMLResponse)
def Db():
  return
