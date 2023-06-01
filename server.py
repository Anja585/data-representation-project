# Module: Data representation
# Author: Anja Antolkovic

from flask import Flask, jsonify



app = Flask(__name__, static_url_path='', static_folder='static_pages')


isins = [{'isin_code' : 'XS1906456220', 
          'issuance_date' : '09/11/2018',
          'maturity_date' : '09/11/2061',
          'issuer_name' : 'International Bank for Reconstruction and Development', 
          'coupon_rate' : 0,
          'denomination' : 'EUR'},
          {'isin_code' : 'XS1833442426', 
          'issuance_date' : '07/06/2018',
          'maturity_date' : '06/06/2024',
          'issuer_name' : 'FMO-Ned.Fin.-Maat.is v.Ontw.NV', 
          'coupon_rate' : 0,
          'denomination' : 'USD'}]


@app.route('/')
def hello(): 
    return 'hello'

# get all
@app.route('/isins')
def get_all(): 
    return jsonify(isins)

# get isin
@app.route('/isins/<isin_code>')
def get_isin_code(isin_code):
    found_isins = list(filter(lambda t : t['isin_code'] == isin_code, isins))
    if len(found_isins) == 0:
        return jsonify({}), 204
    return jsonify(found_isins[0]) 
    
# create isin
@app.route('/isins', methods = ['POST'])
def create_isin(): 
    new_isin = {
          'isin_code' : 'xxx', 
          'issuance_date' : 'ccc',
          'maturity_date' : 'ttt',
          'issuer_name' : 'eee', 
          'coupon_rate' : 0,
          'denomination' : 'EUR'
           }
    isins.append(new_isin)
    return jsonify(new_isin)

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


