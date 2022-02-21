from pydoc import locate
from flask import Flask,request,render_template
import pyshorteners
app=Flask(__name__)

@app.route('/')
def home():
    if request.method == 'GET':
        url=request.args['name']
        print(request.form['location'])
        print(request.form.get['location'])
        #  loca=request.args['location']
        s=pyshorteners.Shortener()
        shorter=s.jdkh.short(url)
        return shorter

    return render_template('link.html')

if __name__=='__main__':
    app.run(debug=True)