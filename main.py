from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello_world():
    return 'this is what you want -- ' +  request.form['text']

@app.route('/order', methods=['POST'])
def hello():
    channel_name=request.form['channel_name']
    return render_template('test.html', channel_name=channel_name)

if __name__ == '__main__':
    app.run()




