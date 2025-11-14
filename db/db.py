import asyncpg

DATABASE_URL = 'postgres://postgres:root@localhost/cforge_package_manager'

async def dbConnectionOpen():
	return await asyncpg.create_pool(DATABASE_URL)


	
