from flask import Flask, render_template, request
from flask.wrappers import Request

def paly_drome(finput): 
        
        chcase = finput.lower()
        rev_input = chcase[::-1]
        if chcase == rev_input:
            return (chcase + " Yes its a Palindrome" )
        else:
            return (chcase + " Sorry its not a Palindrome" )

app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        finput = request.form.get("fname")
        result = paly_drome(finput)
        return render_template('homepage.html', value=result)
    elif request.method == 'GET':        
        return render_template('homepage.html')

#Get Input and change case function


if __name__ == '__main__':
   app.run()
