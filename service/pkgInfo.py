#libs
from fastapi import Request

#modules
from db import db

async def pkgsInfo(pkg_name):
	pool = await db.dbConnectionOpen()
	conn = await pool.acquire()

	#print(pkg_name)
	package_info_constructor = {"existence": False, "name": None, "version": None}

	pkg_info_raw = await conn.fetchrow("select * from packages_list where name = $1", pkg_name)
	#print(pkg_info_raw)
	
	if pkg_info_raw:
		package_info_constructor["existence"] = True
		package_info_constructor["name"] = pkg_info_raw["name"]
		package_info_constructor["version"] = pkg_info_raw["version"]

	await conn.close()
	await pool.close()
	return package_info_constructor




'''

packages_list:

	id: ll (long long I mean) (64 bit)
	name: varchar(255)
	version: varchar(255)
	description: string (AKA text)
	maintainer: varchar(255)
	dependencies: ll -> keeps packages id
	downloads: ll
	server_name: varchar(255) - archive name
	
'''
