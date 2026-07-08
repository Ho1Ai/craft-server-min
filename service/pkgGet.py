from db import db

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
		package_name_getter_constructor["server_name"] = row["server_name"]
		package_name_getter_constructor["version"] = row["version"]
	await conn.close()
	await pool.close()

	return package_name_getter_constructor 

async def resolveFullDependenciesList(pkg_list):
    pool = await db.dbConnectionOpen()
    conn = await pool.acquire()

    pkg_list_id = []

    for pkg in pkg_list:
        pkg_list_id.append(await conn.fetchrow("select id from packages_list where name = $1", pkg))

    pending = set(pkg_list_id)
    result = set()
    checked = set()

    while pending:
        current = pending.pop()

        if current in checked:
            continue

        dependencies = await conn.fetchrow("select dependencies from packages_list where id = $1", current)

        result.update(dependencies)
        pending.update(dependencies)

        checked.add(current)

    if (result == checked):
        print("all dependencies resolved")

    await conn.close()
    await pool.close()