from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/top')
def top():
    return "ここはトップだよ"

@app.route('/hello/<text>')
def namehello(text):
    return text + "さんこんにちは"

@app.route('/index')
def index():
    name="daisuke"
    age=20
    address="田町"
    return render_template('index.html',user_name = name,user_address=address,user_age=age)

@app.route('/weather')
def weather():
    tenki="晴れ"
    return render_template('weather.html',user_tenki=tenki)



if __name__ == '__main__':
    app.run(debug=True)