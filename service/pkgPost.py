from db import db

async def createPackage(pkg_name: str, pkg_version: str, pkg_dependencies: list, pkg_maintainer: str, pkg_description: str, pkg_server_name: str):
	pool = await db.dbConnectionOpen()
	conn = await pool.acquire()

	pkg_creation_status = {"is_ok": True, "status_code": 0}

	check_name_existence = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)
	check_server_name_existence = await conn.fetchrow("select * from packages_list where server_name = $1", pkg_server_name)

	if check_name_existence or check_server_name_existence:
		pkg_creation_status["is_ok"]=False
		pkg_creation_status["status_code"]=5
	else:
		test = await conn.execute("insert into packages_list (name, version, dependencies, maintainer, description, server_name, downloads) values ($1, $2, $3, $4, $5, $6, $7)", pkg_name, pkg_version, pkg_dependencies, pkg_maintainer, pkg_description, pkg_server_name, 0)


	await conn.close()
	await pool.close()
	return pkg_creation_status
	
