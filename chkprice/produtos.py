import msgpack
import falcon
import json
from PIL import Image


class Resource(object):

    def criar_doc():
        return {"produtos": [{"codigo": "1", "produto": "COCA COLA LATA 350ml", "preco": "3, 10", "urlImage": "/images/cocacola.png",
                              "promocao": [
                                  {
                                      "codigo": "1",
                                      "codigoProduto": "1",
                                      "produto": "Coca cola lata 350ml",
                                      "promocao": "Levando 3 latas Coca Cola 350ml a unidade sai por:",
                                      "preco": "2,79",
                                      "urlImage": "/images/cocacola.png",
                                      "desconto": "10"
                                  }
                              ]
                              }
                             ]
                }

    def on_get(self, req, resp):
        doc = criar_doc()

        im = Image.open("./images/cocacola.png")
        d1 = im.size[0]/im.size[1]
        print(d1)

       # Create a JSON representation of the resource
        resp.body = json.dumps(doc)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
