#simple flask application with some endpoints 
from  flask import Flask
app=Flask(__name__)
stores=[
    {'name':'My own private store',
    'items':[
        {'name':'Toilet Paper 18 pack','price':9.0 }
    ]
]
@app.route('/store',methods=['POST'])
def create_store():
    pass 
# get store</<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass 

@app.route('store')
def get_stores():
    pass

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass




app.run(port=5000)