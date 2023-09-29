from fastapi import FastAPI, HTTPException, status
from typing import Optional
from models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "curso BA - ADS",
        "aulas": 10,
        "horas": 60
    },
    2: {
        "titulo": "curso BA - ARQ",
        "aulas": 8,
        "horas": 100
    },
    3: {
        "titulo": "curso BA - MD",
        "aulas": 12,
        "horas": 50
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int):
    try:
        curso = cursos [curso_id]
        curso.update({"Id": curso_id})
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso inexistente')
    return curso

@app.post('/cursos')
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Conflito de ID = {curso.id}')

if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)