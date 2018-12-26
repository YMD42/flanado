[WIP] Flanado - Flask-like API for tornado
===============================

version number: 0.0.1

Overview
--------

This package provides flask-like routes API for tornado web framework.

Installation / Usage
--------------------

To install use pip:

    $ pip install flanado


Or clone the repo:

    $ git clone https://github.com/ymd42/flanado.git
    $ python setup.py install
    

Below is a minimum example which covers a few routes examples in Flask's [Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)

```python
from flanado import Flanado


app = Flanado(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route(r'/user/(?P<username>.*)')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/(?P<post_id>\d+)')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % int(post_id)


@app.route('/path/(?P<subpath>.*)')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.run()
```

( from (example/minimum.py)[example/minimum.py])

You can try it with:
```
python example/minimum.py
```

then tornado server starts at 17755 port. Check it with curl.

```
$ curl localhost:17755/user/42; echo
User 42
```


ToDo
------------

- [x] Basic routing is runnable
- [ ] Support exactly same routing string as Flask ( use werkzeug's routing functions )
- [ ] Support multiple routing for a single method ( like [here](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates) )


Contributing
------------

TBD

Example
-------

TBD
