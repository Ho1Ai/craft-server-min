#libs
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

#handlers
import service.pkgInfo as pkgInfo

global_router = APIRouter(prefix='/api')

@global_router.get('/pkg-info')
async def getPkgInfo(request: Request, name):
	print(name)
	await pkgInfo.pkgsInfo(name)
	return {"is_ok": True,
			"status_code": 0,
			"pkg_name": request.headers}


@global_router.get('/pkg-get')
async def getPkgArchieve():
	pass


