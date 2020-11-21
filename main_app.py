from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate key and create Fernet object with it
key = Fernet.generate_key()
f = Fernet(key)


@app.route('/encrypt')
def encrypt_string():

    """
        Function gets from url string, which need to encrypt.
        And returns html page with encrypted string as bytes inside.
        if user doesn`t provide string - string would be 'default'

    Returns:
        bytes: bytes of encrypted string
        html page: rendered html
    """
    string = request.args.get('string', 'default')
    # For encryption arguments needs to be as bytes data
    encrypted_string = f.encrypt(str.encode(string))
    return render_template('encrypt_page.html', string=encrypted_string)


@app.route('/decrypt')
def decrypt_string():

    """
        Function gets from url string, which need to decrypt as string type.
        And returns html page with decrypted string as string inside.
        if user doesn`t provide string - string would be 'default'

    Returns:
        bytes: bytes of decrypted string
        html page: rendered html
    """
    string = request.args.get('string', 'default')
    # For decryption arguments needs to be as bytes data
    decrypted_bytes = f.decrypt(str.encode(string))
    decrypted_string = str(decrypted_bytes.decode("utf-8"))
    return render_template('decrypt_page.html', string=decrypted_string)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
