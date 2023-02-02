from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def Hello():
  return {
   'message': 'Hello, world!',
   'routes': [
     '/v1/hi?name=yourname',
     '/v1/teapot'
   ]
  }
