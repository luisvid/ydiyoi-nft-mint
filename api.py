from flask import Flask, jsonify, json, request
from brownie import network
#from .scripts.simple_collectible.create_collectible import nftcode
import os

app = Flask(__name__)

#app.register_blueprint(nftcode)

# De la manera en la que mostramos abajo, funciona pero hace un loop infinito, por lo cual abria que ponerlo
# solo cuando el boton de Minting se apriete.
@app.route('/', methods=['GET'])
def index():
    os.system("brownie run scripts/simple_collectible/create_collectible.py  --network rinkeby")
    return {
        'name': 'BAAS 256 PRUEBA API'
    }


"""
Ejemplo Fabri, Obtencion de datos desde el boton.
@app.route('/api', methods=['POST'])
def store():
   #request_data = json.loads(request.data) Esta seria la forma si los parametros son 
   #Pasados de forma de form, en nuestro caso se pasaran como un archuvo de JSON
    data = request.get_json() 
    url = json.loads(data) #Aca convertimos el JSON a un Diccionario de PY
"""

if __name__ == '__main__':
    app.run(debug=True)