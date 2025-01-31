from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from http import HTTPStatus

from fast_zero.schemas import Message
app = FastAPI()


@app.get('/', status_code = HTTPStatus.OK, response_model=Message )
def read_root():
    return {'message': 'Olá Mundo!'}