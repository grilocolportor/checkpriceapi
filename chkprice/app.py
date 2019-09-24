import falcon

from .images import Resource
from .produtos import Resource

api = application = falcon.API()

images = Resource()
produtos = Resource()
api.add_route('/images', images)
api.add_route('/produtos', produtos)
