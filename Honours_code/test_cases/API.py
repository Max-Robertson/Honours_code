from flask import Flask, jsonify, request 

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if (request.method == 'POST'): 
        some_json = request.get_json()  
        return jsonify({'you sent':some_json}), 201 
    else:
        return jsonify({"about":"Hello World"}) 
    
@app.route('/multi/<int:num>', methods=['GET']) 
def get_multiply10(num): 
    return jsonify({"result":num * 10, "result2":num * 2, "result3":num * 100})   

@app.route('/question/<string:question>', methods=['GET']) 
def get_question(question):  
    if (question == "fred"):
        return jsonify({"question":" 'mylk'  is what word put through a caeser cipher ?", "answer": "fred"}) 
    if (question == "bob"):
        return jsonify({"question":" 'ivi'   is what word put through a caeser cipher ?", "answer": "bob"}) 
    if (question == "alice"):
        return jsonify({"question":" 'hspjl'   is what word put through a caeser cipher ?", "answer": "alice"}) 
    if (question == "eve"):
        return jsonify({"question":" 'lcl'   is what word put through a caeser cipher ?", "answer": "eve"})  

if __name__ == '__main__': 
    app.run(debug=True)
    
