from flask import Flask, jsonify, Response, render_template
from flask_restful import Resource, Api, fields, marshal_with
import requests, json
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore 

#setup
#cred = credentials.Certificate( "/home/kswong/movie_api/serviceAccountKey.json")
#firebase_admin.initialize_app(cred)

app = Flask(__name__)

#db=firestore.client()

#Add documents
#data ={'name':'John smith', 'age':40, 'emlopyed': True  }
#db.collection('people').add(data)

#Get all documents in a collection
#docs = db.collection('persons').get()
#for doc in docs:
    #print(doc.to_dict())



@app.route("/")
def hello_world():
    #return redirect("/v1/pokemon/all")
    #return "<p>Hello, World!</p>"
    return render_template('index.html')

#Prints all Pokemon via JSON
@app.route('/v1/pokemon/all', methods=['GET'])
def poke_names():
    data = []
    data2 ={}
    data3 = []
    name_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    #name_url = "https://pokeapi.co/api/v2/ability/?limit=20&offset=20"
    while True:
        resp = requests.get(name_url)
        json = resp.json()
        data.extend(json.get('results', []))
        #data2 = json.get('results', [])
        for count in range(len(data)):         
            data2 = data[count]
            data3.append(data2['name'])  
        name_url = json.get('next')
        if not name_url: break
    return jsonify(data3)


if __name__ == "__main__":
    app.run(debug = True)
