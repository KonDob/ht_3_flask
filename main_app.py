from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/encrypt')
def encrypt_string():
    string = request.args.get('string', 'default')
    return render_template('index.html', string=string)


@app.route('/decrypt')
def decrypt_string(string):
    print(type(string))
    return render_template('index.html', string=string)


@app.route('/')
def catalog():
    return "<h1>Hello Catalog!!!!<h1>"


if __name__ == '__main__':
    app.run(debug=True)
