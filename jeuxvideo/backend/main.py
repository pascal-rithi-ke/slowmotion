import os
from bson import json_util
import json
import pymongo
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv('ID_MONGO')
PASS = os.getenv('PASS_MONGO')

DATABASE_URL = f'mongodb+srv://{ID}:{PASS}@cluster0.mn21l.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(DATABASE_URL)
mydb = client['DataJeux']
mycol = mydb['JeuxVideo']
mycol2 = mydb['test']

# Flask

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
def jeuxvideo():
      output = []
      for x in mycol.find():
              output.append({'id' : x['id'],'name':x['name'],'note': x['note'],'img': x['img'], 'genres': x['genres']})
      """ici"""
      response = jsonify({'results':output})
      response.headers.add("Access-Control-Allow-Origin","*")
      return response

@app.route('/<id>/', methods = ['GET'])
def getInfo(id):
      output = []
      for x in mycol2.find({'id':id}):
        output.append({'id' : x['id']})
      conv = json.loads(json_util.dumps(output))
      response = jsonify({'results':conv})
      response.headers.add("Access-Control-Allow-Origin","*")
      return response

if __name__ == "__main__":
  app.run(host="127.0.0.1", port="5000", debug=True)