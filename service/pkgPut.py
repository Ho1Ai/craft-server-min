from db import db

async def updateDownloads(pkg_name):
	pool = await db.dbConnectionOpen()
	conn = await pool.acquire()

	row = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)

	if row:
		new_downloads = row["downloads"] + 1
		updater = await conn.execute("update packages_list set downloads = $2 where name = $1", row["name"], new_downloads)

	await conn.close()
	await pool.close()
	
