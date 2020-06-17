#python beaker caching
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache = CacheManager(**parse_cache_config_options({
    'cache.type': 'memory',
    'cache.expire': 60
}))
