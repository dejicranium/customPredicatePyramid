from pyramid.config import Configurator
from .predicates import UserAgentPredicate


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.add_view_predicate('device', UserAgentPredicate)
        config.scan()
    return config.make_wsgi_app()
