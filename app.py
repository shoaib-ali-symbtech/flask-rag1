
from flask import Flask,request,jsonify
from data_loader import load_files
from query import query
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

@app.route('/query')
def do_query():
    q = request.args.get('q', '')
    response=query(q)
    
    return jsonify({"query": f"You queried for {q}","result":response})

@app.route('/')
def home():
    return "<h1>Welcome</h1><br/>"

@app.route('/update')
def about():
    return "Will only update manually"
    # res=load_files()
    # return {
    #     # "name":b,
    #     "response":res
    # }




if __name__ == "__main__":
    app.run()