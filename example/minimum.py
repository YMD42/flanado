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
    # show the user profile for that user
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
