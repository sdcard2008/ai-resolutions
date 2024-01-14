from flask import Flask
from flask import render_template as rt

from flask import request
from ai import get_gpt_response
app = Flask(__name__)

@app.route("/" , methods=['GET' , 'POST'])
def index():
    description= None
    if request.method == 'POST':
        
        try:
            description = request.form['desc']
        except:
            pass    
    
    if description:
        response = get_gpt_response(description)
        
        if type(response) != dict or response['code'] == 0:
            response = 'Not enough information provided'
         
    else:
        response = None        
        
    return rt('index.html' , response=response)
