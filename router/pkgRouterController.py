#libs
from fastapi import APIRouter, Request, File, UploadFile, Body
from fastapi.responses import FileResponse
import os

#handlers
import service.pkgInfo as pkgInfo
import service.pkgPost as pkgPost
import service.pkgGet as pkgGet
import service.pkgPut as pkgPut

from models import default_models as models
from service import pkgCountHash

global_router = APIRouter(prefix='/api')
#
# @global_router.get('/pkg-info')
# async def getPkgSingleInfo(request: Request, name):
# 	#print(name)
# 	data = await pkgInfo.pkgsInfo(name)
# 	#print(data['version'], data["existence"])
# 	return {"is_ok": True,
# 			"status_code": 0,
# 			"existence": data.get("existence"),
# 			"version": data.get("version")
# 			}
#

@global_router.get('/check-pkg-existence')
async def checkPkgExistence(request: Request):
    result = await pkgGet.checkPkgExistence(request)
    return {"existence": result}

@global_router.get('/pkg-get')
async def getPkgArchieve(request: Request):
    pkg_name = request.headers["pkg_name"]
    pkg_server_name_getter = await pkgGet.getPkgPath(pkg_name)

    if pkg_server_name_getter["existence"]:
        if os.path.exists(pkg_server_name_getter['server_name']):
            pkg_len = os.path.getsize(pkg_server_name_getter.get['server_name'])
            pkg_hash = pkgCountHash.countFileHash(pkg_server_name_getter['server_name'])
            new_file = pkg_server_name_getter['server_name']
            return FileResponse(new_file, headers={"App-Pkg-Version": pkg_server_name_getter["version"], "App-Pkg-Size": pkg_len, "App-Pkg-Hash": pkg_hash})
        else:
            return {"is_ok": False, "status_code": 11}
    else:
        return {"is_ok": False, "status_code": 11}
#
# @global_router.post('/pkg-post-test')
# async def test_post (package_file: UploadFile = File(...)):
#     contents = await package_file.read()
#
#     # pkg_count_hash = pkgCountHash.countFileHash(contents)
#
#     print(len(contents))

# @global_router.post('/add-package')
# async def createPackage(new_pkg_creation_instance: models.CreationModel = Body(...), package_file: UploadFile = File(...)):
#     hashed_pkg_update_key = pkgCountHash.pkgHexifier(new_pkg_creation_instance.pkg_update_key)
#     new_pkg_name = new_pkg_creation_instance.pkg_name.lower().replace(" ", "-")
#
#     new_pkg_server_path = new_pkg_creation_instance.pkg_name.lower()+'-'+new_pkg_creation_instance.pkg_version.lower()
#
#     contents = await package_file.read()
#     with open(new_pkg_server_path, 'wb') as f:
#         f.write(contents)
#
#     pkg_count_hash = pkgCountHash.countFileHash(contents)
#
#     print(pkg_count_hash, len(contents), hashed_pkg_update_key, new_pkg_server_path)
#
#     status = await pkgPost.createPackage(pkg_name=new_pkg_name,
# 	    pkg_version=new_pkg_creation_instance.pkg_version,
# 	    pkg_dependencies=new_pkg_creation_instance.pkg_dependencies,
# 	    pkg_maintainer=new_pkg_creation_instance.pkg_maintainer,
# 	    pkg_server_path=new_pkg_server_path,
# 	    pkg_update_key=hashed_pkg_update_key,
#         pkg_hash=pkg_count_hash,
#         pkg_size=len(contents))
#     return status

@global_router.post("/request-pkg-add")
async def requestPkgAdd(request: models.RequestPkgAdd):
    result = {"is_ok": True, "status_code": 0}
    return result

@global_router.get("/get-pkg-dependencies")
async def getPkgDependencies(name: str):
    result = pkgGet.resolveFullDependenciesList(name)
    return {"dependencies": result}

@global_router.post('/get-pkg-data')
async def getPkgData(pkg_list: models.RequestList):
    # full_dependencies_list = await pkgGet.resolveFullDependenciesList(pkg_list.package_list)
    final_array = []
    for pkg in pkg_list.package_list:
        pkg_data = await pkgGet.getPkgData(pkg)
        final_array.append(pkg_data)

    result = {"packages": final_array}
    return result