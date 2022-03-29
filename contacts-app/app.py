from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.17.0.2:27017/contacts"
mongo = PyMongo(app)
data_collection = mongo.db.contact

@app.route('/')
def form():
    return render_template('form.html')


@app.route('/data', methods=['GET'])
def show_data():
    if request.method == 'GET':
        name = request.args.get("x")
        phone = request.args.get("y")
        if name != "" and phone != "":
            data_collection.insert_one({"name": name, "phone":phone})
            return("Contact has been Added.")
        else:
            return("Fill the form correctly....!!!!")

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/display')
def display():
    name = request.args.get("z")
    user = data_collection.find_one_or_404({'name' : name})
    return render_template('index.html', customer = user)

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/drop')
def drop():
    name = request.args.get("z")
    data_collection.delete_one({'name': name})
    return ('User has been deleted.')

if __name__ == '__main__':
   app.run(debug = True)
