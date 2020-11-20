from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate key and create Fernet object with it
key = Fernet.generate_key()
f = Fernet(key)


@app.route('/encrypt')
def encrypt_string():
    """ 
        Functions get from url string, which need to encrypt. 
        And returns encrypted string as bytes.

    Returns:
        bytes: bytes of encrypted string
    """
    string = request.args.get('string', 'default')
    # For encryption arguments needs to be as bytes data
    encrypted_string = f.encrypt(str.encode(string))
    return render_template('encrypt_page.html', string=encrypted_string)


@app.route('/decrypt')
def decrypt_string():
    """ 
        Functions get from url string, which need to decrypt as string type. 
        And returns decrypted string as string.

    Returns:
        string: decrypted string
    """
    string = request.args.get('string', 'default')
    # For encryption arguments needs to be as bytes data
    decrypted_bytes = f.decrypt(str.encode(string))
    decrypted_string = str(decrypted_bytes.decode("utf-8"))
    return render_template('decrypt_page.html', string=decrypted_string)


@app.route('/')
def catalog():
    return "<h1>Hello Catalog!!!!<h1>"


if __name__ == '__main__':
    app.run(debug=True)
