from pydantic import BaseModel

class CreationModel(BaseModel):
	pkg_name: str
	pkg_version: str
	pkg_dependencies: list
	pkg_maintainer: str
	pkg_description: str
	pkg_server_name: str
'''
class DownloadPackageRequest(BaseModel):
	pkg_name: str
'''
