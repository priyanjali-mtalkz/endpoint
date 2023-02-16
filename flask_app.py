from flask import *
import random
from prime import *
import json
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
# app.json_encoder = LazyJSONEncoder


# swagger_template = dict(
# info = {
#     'title': LazyString(lambda: 'Get a list of random numbers'),
#     'version': LazyString(lambda: '0.1'),
#     'description': LazyString(lambda: 'This document depicts a sample Swagger UI document and implements Hello World functionality after executing GET.'),
#     },
    
#     host = LazyString(lambda: request.host)
# )


# swagger_config = {
#     "headers": [],
#     "specs": [
#         {
#             "endpoint": 'random',
#             "route": '/random',
#             "rule_filter": lambda rule: True,
#             "model_filter": lambda tag: True,
#         }
#     ],
#     "static_url_path": "/flasgger_static",
#     "swagger_ui": True,
#     "specs_route": "/apidocs/"
# }
# swagger = Swagger(app, template=swagger_template,             
#                   config=swagger_config)


#@swag_from("random.yml", methods=['GET'])
# @app.route('/random/<int:num>',methods = ['GET'])
# def get_random(num):
#     """
#     paths:
#   /random/{num}:
#     get: body
#       parameters:
#         - in: 
#           name: num   # Note the name is the same as in the path
#           required: true
#           type: integer
#           minimum: 1
#           description: The user ID.
#        responses:
#          200:
#            description: OK

#     """
#     num = request.get_json['num']
#     arr =[]
#     if num >= 0 and num <= 1000:
#         for i in range(num):
#             n = random.randint(1,1000)
#             if n not in arr:
#                 arr.append(n)
#     return json.dumps(arr)

@app.route('/random/<num>/')
def random_num(num):
    """Example endpoint returning a list of random numbers
    ---
    parameters:
      - name: num
        in: path
        type: integer
        required: true
    responses:
      200:
        description: A list of random numbers 
        schema:
              type: array
              items:
                  type: integer
    """
    num = int(num)
    arr =[]
    if num >= 0 and num <= 1000:
        for i in range(num):
            n = random.randint(1,1000)
            if n not in arr:
                arr.append(n)
    return json.dumps(arr)

if __name__ == '__main__':
    app.run(debug=True)