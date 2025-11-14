#libs
from fastapi import FastAPI

#routers
from router import pkgRouterController as global_controller

app = FastAPI()
app.include_router(global_controller.global_router)

@app.get('/')
def default_out():
	return("The server is started on 127.0.0.1:8000")
