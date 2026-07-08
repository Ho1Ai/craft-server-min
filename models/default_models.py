from pydantic import BaseModel

class CreationModel(BaseModel):
    pkg_name: str
    pkg_version: str
    pkg_dependencies: list
    pkg_maintainer: str
    pkg_update_key: str
'''
class DownloadPackageRequest(BaseModel):
	pkg_name: str
'''

class RequestList(BaseModel):
    package_list: list

class RequestPkgAdd(BaseModel):
    package_name: str
    package_version: str
    package_dependencies: list
    package_maintainer: str