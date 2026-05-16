from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
db_tareas = {}
task_id = 1

class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

@app.get("/tasks")
def get_tasks():
    """retorna todas las tareas"""
    return db_tareas

@app.post("/tasks")
def crear_tarea(task: TareaCreate):
    """crea tarea nueva"""
    global task_id

    # Verificar si ya existe una tarea con el mismo título
    for tarea in db_tareas.values():
        if tarea["titulo"].lower() == task.titulo.lower():
            raise HTTPException(
                status_code=400,
                detail="La tarea ya existe"
            )

    nueva_tarea = Tarea(
        id=task_id,
        titulo=task.titulo,
        descripcion=task.descripcion
    )

    db_tareas[task_id] = nueva_tarea.model_dump()

    task_id += 1

    return {
        "mensaje": "Tarea creada con éxito"
    }


 