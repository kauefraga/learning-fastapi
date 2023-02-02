from fastapi import APIRouter

router = APIRouter()

@router.get('/hi')
def Hi(name: str = ''):
  return {
    'Message': 'Hi! ' + name
  }
