#%%
from redis_client import redis_client
#%%
redis_client.set('Artem', 'Poltavskii')

# %%
redis_client.get('Artem')

# %%
