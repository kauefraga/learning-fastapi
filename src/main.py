import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def Hello():
  return {'Hello': 'world'}

@app.get('/teapot', response_class=HTMLResponse)
def teapot():
  data = requests.get('http://httpbin.org/status/418').text
  return '<pre>'+data+'</pre>'
