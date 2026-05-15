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

@app.post("/tasks")
def crear_task(task: Tarea):
    global task_id
    task_id += 1
    """crea una tarea nueva"""
    
    nuevo_id = task_id

    db_tareas[nuevo_id] = task.model_dump()

    return {"mensaje": "Tarea creada con exito"}






"""    if usuario.user_id in usuarios_db:
        raise HTTPException(status_code=400, detail="El ID de usuario ya existe")
    
    # Agregar al diccionario de diccionarios
    usuarios_db[usuario.user_id] = {
        "nombre": usuario.nombre,
        "rol": usuario.rol
    }"""