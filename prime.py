from flask import *
from prime import *
import json
from flasgger import Swagger
import math

app = Flask(__name__)
swagger = Swagger(app)


class isPrime():
    def check(n):
        if n <= 1:
            return False
        for i in range(2,int(math.sqrt(n)+2)):
            if(n%i)== 0:
                return False
            else:
                return True

@app.route('/prime/<num>/')
def prime_num(num):
    """Example endpoint returning a list of prime numbers
    ---
    parameters:
      - name: num
        in: path
        type: integer
        required: true
    responses:
      200:
        description: A list of prime numbers 
        schema:
              type: array
              items:
                  type: integer
    """
    num = int(num)
    arr = []
    i = 2    
    if num >= 0 and num <= 1000:
        while(len(arr) < num):
            if isPrime.check(i):
                arr.append(i)   
            i += 1
    return json.dumps(arr)

if __name__ == '__main__':
    app.run(debug=True)