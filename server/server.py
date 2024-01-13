from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/crawl', methods = ['POST'])
def post_crawl(): 
    if(request.method == 'POST'): 
        data = {"id": "30vbllyb"}
  
        return jsonify(data) 
    
@app.route('/crawl/<id>', methods = ['GET'])
def get_crawl(id): 
    if(request.method == 'GET'): 
        data = {
                "id": id,
                "status": "active",
                "urls": [
                "http://hiring.axreng.com/index2.html",
                "http://hiring.axreng.com/htmlman1/chcon.1.html"
                ]
        }
  
        return jsonify(data) 

app.run(host='0.0.0.0', port=4567)
