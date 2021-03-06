from flask import Flask, jsonify, request
import pyrebase
import os as os


from flask import Flask, jsonify, request
import pickle


config={
    "apiKey": "AIzaSyDeFLJFr2aqcAK40nZOmBtEDNYij49yyAk",
    "authDomain": "healdon-916dd.firebaseapp.com",
    "databaseURL": "https://healdon-916dd.firebaseio.com",
    "projectId": "healdon-916dd",
    "storageBucket": "healdon-916dd.appspot.com",
    "messagingSenderId": "************",
    "appId": "********************************"
}
firebase=pyrebase.initialize_app(config)

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    path=os.getcwd()
    
    storage = firebase.storage()
    storage.child("Audio/27 sec clip.wav").download("downloaded.wav")
    # predictions
    #result = model.predict(data_df)

    # send back to browser
    #output = {'results': int(result[0])}
    output = {'results': path}
    
    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True,use_reloader=False)
