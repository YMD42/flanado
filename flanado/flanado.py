import logging

import tornado.web


logger = logging.getLogger(__name__)


class Flanado:
    def __init__(self, name):
        self.name = name
        self.handlers = []

    def route(self, path, methods=['GET']):
        def build_handler(f):
            def wrapped_to_handle_self(self_, *args, **kwargs):
                self_.write(f(*args, **kwargs))

            handler_class = type(
                '%sBaseHandler' % self.name, 
                (tornado.web.RequestHandler,),
                {method.lower() : wrapped_to_handle_self
                 for method in methods})

            self.handlers.append((path, handler_class))
        return build_handler

    def run(self, port=None, host=None):
        host = host if host else 'localhost'
        port = port if port else 17755

        for i, (path, handler) in enumerate(self.handlers):
            logger.debug('handler definition %d : %s -> %s' %
                         (i, path, handler))
            logger.debug(handler.__dict__)

        app = tornado.web.Application(self.handlers)
        
        logger.debug('Start serving. host = %s, port = %s' % (host, port))

        app.listen(address=host, port=port)
        tornado.ioloop.IOLoop.current().start()
    
