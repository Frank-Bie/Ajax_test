from flask import Flask,render_template,request
from flask import jsonify
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testGet')
def ajaxGet():
    return str(int(request.args['msc'])*2)
 
@app.route('/testPost', methods=['POST'])
def ajaxPost():
    number = int(request.values['msc']) + 1
    print(number)
    return jsonify({'msc':number,'小红':number+1,'小绿':number+2})
    
@app.route('/testPostII/<number>',methods=['POST'])
def ajaxPostII(number):
    return jsonify({"result":int(number)+1})
app.run()