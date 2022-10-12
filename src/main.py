import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def Hello():
  return {
   'message': 'Hello, world!',
   'routes': ['/hi', '/teapot']
  }

@app.get('/hi')
def Hi(name: str = ''):
  return {
    'Message': 'Hi! ' + name
  }

@app.get('/teapot', response_class=HTMLResponse)
def Teapot():
  data = requests.get('https://httpbin.org/status/418').text
  return '<pre>'+data+'</pre>'
