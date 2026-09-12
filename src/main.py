from fastapi import FastAPI
from routers.users import router as user_router
from routers.boards import router as board_router
from routers.tasks import router as task_router

app = FastAPI()

app.include_router(user_router)
app.include_router(board_router)
app.include_router(task_router)
