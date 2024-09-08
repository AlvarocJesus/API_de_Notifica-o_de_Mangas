from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
  return {'Hello': 'World'}

@app.get('/mangas')
async def get_mangas():
  return [{'title': 'One Piece'}, {'title': 'Naruto'}]

@app.post('/mangas')
async def save_manga(manga: dict):
  return manga