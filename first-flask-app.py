from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "hello word once again !!! "

app.run(port=5000)