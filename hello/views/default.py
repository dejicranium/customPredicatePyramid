from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .. import models

@view_config(route_name="home", renderer="json")
def home_desktop(request):
    return {"status": "This is the homepage for desktop devices"}

@view_config(route_name="home", renderer="json", device="mobile")
def home_mobile(request):
    return {"status": "This is the homepage for mobile devices"}
