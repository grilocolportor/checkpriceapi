import msgpack
import falcon

class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'images' : [
                {
                    'href' : '/images/cocacola.png'
                }
            ]
        }

        resp.data = msgpack.packb(doc, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200