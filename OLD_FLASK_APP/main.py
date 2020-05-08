from flask import Flask, jsonify, render_template, redirect, current_app, request, flash
from pymongo import MongoClient
from bson.json_util import dumps
import new_prop
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField



app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

username = 'read_only'
password = 'rJMef22QkRqPDFzk'
client = MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0-paegd.mongodb.net/test?retryWrites=true&w=majority")
db = client.rental_db

property_collection = db['properties']
properties = [acct for acct in property_collection.find()]




@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', data=properties)


@app.route('/api/new_property', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        form = request.form
        prop_id = new_prop.new_property(form);
        print(prop_id)
        properties = [acct for acct in property_collection.find()]
        return render_template('property.html', data=properties)
    else:
        return render_template('index.html', data=properties)

@app.route('/api/properties',methods=['GET'])
def api_properties():
    property_list = list(properties)
    return current_app.response_class(dumps(property_list), mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)
