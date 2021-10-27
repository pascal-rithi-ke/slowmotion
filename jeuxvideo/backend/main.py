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

#x = mycol.find_one()
#for x in mycol.find():
#  print(x)

# Flask

app = Flask(__name__)
CORS(app)

@app.route("/")
def detail():
  #List all Video games plus some details
  output = []
  for x in mycol.find():
    output.append(x)
  #Return the data array as JSON format
  conv = json.loads(json_util.dumps(output))
  response = jsonify({'results':conv})
  response.headers.add("Access-Control-Allow-Origin","*")
  return response

if __name__ == "__main__":
  app.run(host="127.0.0.1", port="5000", debug=True)