# Module: Data representation
# Author: Anja Antolkovic

from flask import Flask


app = Flask(__name__, static_url_path='', static_folder='static_pages')


@app.route('/')
def hello(): 
    return 'hello'

# get all
@app.route('/isins')
def get_all(): 
    return 'served by get_all()'

# get isin
@app.route('/isins/<isin_code>')
def get_isin_code(isin_code): 
    return 'served by get_isin_code()' + ' ' + str(isin_code)

# create isin
@app.route('/isins', methods = ['POST'])
def create_isin(): 
    return 'served by create_isin()'

# update isin
@app.route('/isins/<isin_code>', methods = ['PUT'])
def update_isin(isin_code): 
    return 'served by update_isin()' + ' ' + str(isin_code)

# delete isin
@app.route('/isins/isin_code', methods = ['DELETE'])
def delete_isin(isin_code): 
    return 'served by delete_isin()' + ' ' + str(isin_code)


if __name__ == '__main__':
    app.run(debug=True)
