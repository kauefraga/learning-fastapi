import httpx
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get('/teapot', response_class=HTMLResponse)
def Teapot():
  data = httpx.get('https://httpbin.org/status/418').text
  return '<pre>'+data+'</pre>'
