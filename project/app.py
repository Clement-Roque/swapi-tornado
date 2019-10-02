import tornado.ioloop as t_ioloop
import tornado.web as t_web
import tornado.httpserver as t_httpserver
import handlers
import settings


def make_swapi_rest_api():

    urls = [
        (settings.PEOPLE_URL, handlers.SWAPIPeopleHandler),
    ]

    return t_web.Application(urls)


if __name__ == "__main__":
    swapi_rest_api = make_swapi_rest_api()
    swapi_server = t_httpserver.HTTPServer(swapi_rest_api)
    swapi_server.listen(settings.SWAPI_API_SERVER_PORT)
    t_ioloop.IOLoop.current().start()
