#libs
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
import os

#handlers
import service.pkgInfo as pkgInfo
import service.pkgPost as pkgPost
import service.pkgGet as pkgGet
import service.pkgPut as pkgPut
from models import default_models as models

global_router = APIRouter(prefix='/api')

@global_router.get('/pkg-info')
async def getPkgInfo(request: Request, name):
	#print(name)
	data = await pkgInfo.pkgsInfo(name)
	#print(data['version'], data["existence"])
	return {"is_ok": True,
			"status_code": 0,
			"existence": data.get("existence"),
			"version": data.get("version")
			}


@global_router.get('/pkg-get')
async def getPkgArchieve(request: Request):
	pkg_name = request.headers["pkg_name"]
	pkg_server_name_getter = await pkgGet.getPkgPath(pkg_name)

	if pkg_server_name_getter["existence"]:
		if os.path.exists("./pkg_dir/" + pkg_server_name_getter['server_name']):
			new_file = "./pkg_dir/"+pkg_server_name_getter['server_name']
			return FileResponse(new_file)
		else:
			return {"is_ok": False, "status_code": 11}
	else:
		return {"is_ok": False, "status_code": 11}

@global_router.post('/add-package')
async def createPackage(new_pkg_creation_instance: models.CreationModel):
	status = await pkgPost.createPackage(new_pkg_creation_instance.pkg_name,
	new_pkg_creation_instance.pkg_version,
	new_pkg_creation_instance.pkg_dependencies,
	new_pkg_creation_instance.pkg_maintainer,
	new_pkg_creation_instance.pkg_description,
	new_pkg_creation_instance.pkg_server_name)
	return status

@global_router.put("/update-package-info")
async def updatePkgInfo():
	pass

@global_router.put("/update-downloads")
async def updateDownloads(pkg_name: str):
	await pkgPut.updateDownloads(pkg_name)
	return {"is_ok": True}
