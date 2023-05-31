# Module: Data representation
# Author: Anja Antolkovic

from flask import Flask


app = Flask(__name__, static_url_path='', static_folder='static_pages')

@app.route('/')
def index(): 
    return 'hello'


if __name__ == '__main__':
    app.run()
