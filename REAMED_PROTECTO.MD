Proyecto de portafolio — Fase 1
Ahora construyes algo que va a tu GitHub. Un proyecto completo que cualquier reclutador puede ver.
API de gestión de tareas (To-Do API)
Endpoints a implementar:
GET    /tasks           → listar todas las tareas
GET    /tasks/{task_id} → obtener una tarea por id
POST   /tasks           → crear una tarea
PUT    /tasks/{task_id} → actualizar una tarea completa
DELETE /tasks/{task_id} → eliminar una tarea
Modelo de tarea:
id        → entero
titulo    → string, obligatorio
descripcion → string, opcional
completada  → booleano, por defecto False
Reglas:

Base de datos simulada con diccionario
Manejo de errores 404 cuando la tarea no existe
Conventional commits desde el primer archivo
Cada endpoint en su propio commit