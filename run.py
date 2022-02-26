import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

import manager
import application
from tables import metadata


async def test_connections(conf):  
    row = 'postgresql+asyncpg://{0}:{1}@localhost/{2}'.format(
        conf["database"]["user"],
        conf["database"]["pass"],
        conf["database"]["db"]
    )    
    engine = create_async_engine(row)
    
    async with engine.begin() as conn:        
        await conn.run_sync(metadata.create_all)

        # await conn.execute(
        #     t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        # )
    await engine.dispose()
    
async def test_manager(conf):
    manage = manager.get_manager()




asyncio.run(test_manager(application.get_conf()))