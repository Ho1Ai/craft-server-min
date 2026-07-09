from db import db
import os

async def getPkgPath(pkg_name):
	pool = await db.dbConnectionOpen()
	conn = await pool.acquire()
	
	package_name_getter_constructor = {
		"existence": False,
		"server_name": None,
		"version": None
		}

	row = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)

	if row:
		package_name_getter_constructor["existence"] = True
		package_name_getter_constructor["server_name"] = row["pkg_server_path"]
		package_name_getter_constructor["version"] = row["version"]
	await conn.close()
	await pool.close()

	return package_name_getter_constructor 

async def resolveFullDependenciesList(pkg_name):
    print(pkg_name)
    pool = await db.dbConnectionOpen()
    conn = await pool.acquire()

    result_id = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)

    result_id = result_id["dependencies"]

    result = []
    for dependency in result_id:
        elem_name = await conn.fetchrow("select * from packages_list where id = $1", dependency)

        result.append(elem_name)

    await conn.close()
    await pool.close()

    return result

async def checkPkgExistence(pkg_name):
    pool = await db.dbConnectionOpen()
    conn = await pool.acquire()

    result = False

    pkg_instance = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)

    if pkg_instance:
        result = True

    await conn.close()
    await pool.close()

    return result

async def getPkgData(pkg_name):
    pool = await db.dbConnectionOpen()
    conn = await pool.acquire()

    result = {"name": "", "version": "", "pkg_size": 0}

    pkg_full_row = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)

    if pkg_full_row:
        result["id"] = pkg_full_row["id"]
        result["name"] = pkg_full_row["name"]
        result["version"] = pkg_full_row["version"]
        result["pkg_size"] = os.path.getsize(pkg_full_row['pkg_server_path'])

    await conn.close()
    await pool.close()

    return result