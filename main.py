from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
db_tareas = {}
task_id = 0


class Tarea(BaseModel):
    titulo: str
    descripcion: str | None
    completada: bool = False

@app.get("/tasks")
def get_tasks():
    """retorna todas las tareas"""
    return db_tareas
