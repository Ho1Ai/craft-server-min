import asyncpg

DATABASE_URL = 'postgres://postgres:root@localhost/craft_package_manager_minimal'

async def dbConnectionOpen():
	return await asyncpg.create_pool(DATABASE_URL)


	
