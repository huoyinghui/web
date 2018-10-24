#### cache

[django-redis](https://django-redis-chs.readthedocs.io/zh_CN/latest/#)

#### 设计流程
view
```
given a URL, try finding that page in the cache
if the page is in the cache:
    return the cached page
else:
    generate the page
    save the generated page in the cache (for next time)
    return the generated page

```


#### demo
```
>>> from django.core.cache import cache
>>> cache
<django.core.cache.DefaultCacheProxy object at 0x106c38630>
>>> cache.set('a', 1)
True
>>> cache.get('a')
1
>>>

```

[三种缓存](https://blog.csdn.net/AbeBetter/article/details/78417879)
#### view缓存
```

```

#### Basecache
* KEY_PREFIX
* VERSION
* KEY_FUNCTION

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{host}:{port}'.format(
            host=REDIS.get('default', {}).get('HOST', ''),
            port=REDIS.get('default', {}).get('PORT', ''),
            db=REDIS.get('default', {}).get('DB', ''),
        ),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "{}".format(REDIS.get('default', {}).get('PASSWORD', '')),
        },
        'KEY_PREFIX': 'web',  # 缓存key的前缀（默认空）
        'VERSION': 1,
    },
}
```
```
class BaseCache:
    def __init__(self, params):
        timeout = params.get('timeout', params.get('TIMEOUT', 300))
        if timeout is not None:
            try:
                timeout = int(timeout)
            except (ValueError, TypeError):
                timeout = 300
        self.default_timeout = timeout

        options = params.get('OPTIONS', {})
        max_entries = params.get('max_entries', options.get('MAX_ENTRIES', 300))
        try:
            self._max_entries = int(max_entries)
        except (ValueError, TypeError):
            self._max_entries = 300

        cull_frequency = params.get('cull_frequency', options.get('CULL_FREQUENCY', 3))
        try:
            self._cull_frequency = int(cull_frequency)
        except (ValueError, TypeError):
            self._cull_frequency = 3

        self.key_prefix = params.get('KEY_PREFIX', '')
        self.version = params.get('VERSION', 1)
        self.key_func = get_key_func(params.get('KEY_FUNCTION'))
```


####
```
class RedisCache(BaseCache):
    def __init__(self, server, params):
        super(RedisCache, self).__init__(params)
        self._server = server
        self._params = params

        options = params.get("OPTIONS", {})
        self._client_cls = options.get("CLIENT_CLASS", "django_redis.client.DefaultClient")
        self._client_cls = load_class(self._client_cls)
        self._client = None

```


backend_cls: 就是配置的'django_redis.cache.RedisCache'

```
def _create_cache(backend, **kwargs):
    try:
        # Try to get the CACHES entry for the given backend name first
        try:
            conf = settings.CACHES[backend]
        except KeyError:
            try:
                # Trying to import the given backend, in case it's a dotted path
                import_string(backend)
            except ImportError as e:
                raise InvalidCacheBackendError("Could not find backend '%s': %s" % (
                    backend, e))
            location = kwargs.pop('LOCATION', '')
            params = kwargs
        else:
            # CACHE配置的字典
            params = conf.copy()
            params.update(kwargs)
            # 'django_redis.cache.RedisCache'
            backend = params.pop('BACKEND')
            # 'redis://127.0.0.1:6379/0'
            location = params.pop('LOCATION', '')
        backend_cls = import_string(backend)
    except ImportError as e:
        raise InvalidCacheBackendError(
            "Could not find backend '%s': %s" % (backend, e))
    return backend_cls(location, params)

```

模块变量:cache, 第一次导入就会创建
```
class CacheHandler:
    """
    A Cache Handler to manage access to Cache instances.

    Ensure only one instance of each alias exists per thread.
    """
    def __init__(self):
        self._caches = local()

    def __getitem__(self, alias):
        try:
            return self._caches.caches[alias]
        except AttributeError:
            self._caches.caches = {}
        except KeyError:
            pass

        if alias not in settings.CACHES:
            raise InvalidCacheBackendError(
                "Could not find config for '%s' in settings.CACHES" % alias
            )

        cache = _create_cache(alias)
        # DefaultCacheProxy中调用
        self._caches.caches[alias] = cache
        return cache

    def all(self):
        return getattr(self._caches, 'caches', {}).values()


caches = CacheHandler()
```

#### cache.get/set
get/set 同过代理操作
```
class DefaultCacheProxy:
    """
    Proxy access to the default Cache object's attributes.

    This allows the legacy `cache` object to be thread-safe using the new
    ``caches`` API.
    """
    def __getattr__(self, name):
        return getattr(caches[DEFAULT_CACHE_ALIAS], name)

    def __setattr__(self, name, value):
        return setattr(caches[DEFAULT_CACHE_ALIAS], name, value)

    def __delattr__(self, name):
        return delattr(caches[DEFAULT_CACHE_ALIAS], name)

    def __contains__(self, key):
        return key in caches[DEFAULT_CACHE_ALIAS]

    def __eq__(self, other):
        return caches[DEFAULT_CACHE_ALIAS] == other
```
写数据到redis:
django_redis.client.default.DefaultClient
```
class DefaultClient(object):
   def set(self, key, value, timeout=DEFAULT_TIMEOUT, version=None, client=None, nx=False, xx=False):
        """
        Persist a value to the cache, and set an optional expiration time.
        Also supports optional nx parameter. If set to True - will use redis setnx instead of set.
        """
        nkey = self.make_key(key, version=version)
        nvalue = self.encode(value)

        if timeout == DEFAULT_TIMEOUT:
            timeout = self._backend.default_timeout

        original_client = client
        tried = []
        ...
                if not client:
                    client, index = self.get_client(write=True, tried=tried, show_index=True)

                return client.set(nkey, nvalue, nx=nx, px=timeout, xx=xx)
```


#### 使用缓存
view: 函数中，直接使用cache获取'data'
cache_page: 把整个get/post方法返回的响应缓存30*1s,
```
@method_decorator(cache_page(30 * 1), name='dispatch')
class LoginView(View):
    """

    """
    def get(self, request):
        data = cache.get('data')
        if data:
            logger.debug('cache hit :{}'.format(data))
            return JsonResponse({'hello': data})
        else:
            logger.debug('cache unhit :{}'.format(data))
            data = ["{}".format(i) for i in range(3)]
            cache.set('data', data, timeout=10)
            return JsonResponse({'hello': data})
        redirect_url = request.GET.get('next', '')

        return render(request, "login.html", {
            "redirect_url": redirect_url
        })
```
