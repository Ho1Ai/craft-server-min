#libs
from fastapi import Request

#modules
from db import db

async def pkgsInfo(pkg_name):
	pool = await db.dbConnectionOpen()
	conn = await pool.acquire()

	print(pkg_name)

	conn.close()
	pool.close()
	return packages_info
