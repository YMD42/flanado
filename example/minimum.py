from flanado import Flanado
app = Flanado(__name__)

@app.route(r'/.*')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    app.run()
