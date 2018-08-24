from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data/<name>')
def getData(name):

   with open('data/'+name) as f:
        jsonFile = json.load(f)

   return jsonify(jsonFile)

@app.route('/data/postMethod' , methods=['POST'])
def getDataFromFunction():

   a = request.get_json()
   result= functionPrueba(900,a, "dato")

   return json.dumps(result)

if __name__ == "__main__":
   app.run(host='localhost', port=5001, debug=True)
