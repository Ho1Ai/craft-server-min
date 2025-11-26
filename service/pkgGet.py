from db import db

async def getPkgPath(pkg_name):
	pool = await db.dbConnectionOpen()
	conn = await pool.acquire()
	
	package_name_getter_constructor = {
		"existence": False,
		"server_name": None
		}

	row = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)

	if row:
		package_name_getter_constructor["existence"] = True
		package_name_getter_constructor["server_name"] = row["server_name"]
	await conn.close()
	await pool.close()

	return package_name_getter_constructor 
