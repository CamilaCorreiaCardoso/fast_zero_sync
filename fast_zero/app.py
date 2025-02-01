from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserSchema,UserPublic,UserDB
app = FastAPI()

database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/olamundo', response_class=HTMLResponse)
def read_html():
    return """
    <html>
    <body>
    <h1> Hello World</h1>
    </body>
    </html>
"""


@app.post('/users', status_code= HTTPStatus.CREATED, response_model=UserPublic)
def create_users(user: UserSchema):
    
    user_with_id = UserDB(
        id = len(database) + 1,
        **user.model_dump()
    )
    database.append(user_with_id)
    return user_with_id

