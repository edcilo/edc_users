from fixture import app
from helpers import RedisWrapper
from ms.db.cache import Cache


def test_cache_set_get(app):
    assert app.cache.set("foo", "bar") == True
    res = app.cache.get_raw("foo")
    assert "data" in res
    assert app.cache.get("foo") == "bar"


def test_cache_delete(app):
    app.cache.set("foo", "bar")
    assert app.cache.get("foo") == "bar"
    app.cache.delete("foo")
    assert app.cache.get("foo") is None


def test_cache_truncate(app):
    app.cache.set("foo", "bar")
    app.cache.set("zoo", "zing")
    assert app.cache.get("foo") == "bar"
    assert app.cache.truncate() == True
    assert app.cache.get("foo") is None


def test_cache_exists(app):
    assert app.cache.exists("foo") == False
    app.cache.set("foo", "bar")
    assert app.cache.exists("foo") == True


def test_cache_ping(app):
    assert app.cache.ping() == True
