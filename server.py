# Module: Data representation
# Author: Anja Antolkovic

from flask import Flask, jsonify, request, abort



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
    if not request.json: 
          abort(400)
    new_isin = {
          "isin_code" : request.json["isin_code"], 
          "issuance_date" : request.json["issuance_date"],
          "maturity_date" : request.json["maturity_date"],
          "issuer_name" : request.json["issuer_name"], 
          "coupon_rate" : request.json["coupon_rate"],
          "denomination" : request.json["denomination"]
           }
    isins.append(new_isin)
    return jsonify(new_isin)

# update isin
@app.route('/isins/<isin_code>', methods = ['PUT'])
def update_isin(isin_code):
    found_isins = list(filter(lambda t : t['isin_code'] == isin_code, isins))
    if len(found_isins) == 0:
          return jsonify({}), 404
    current_isin = found_isins[0]
    if "isin_code" in request.json:
          current_isin["isin_code"] = request.json["isin_code"]
    if "issuance_date" in request.json:
          current_isin["issuance_date"] = request.json["issuance_date"]
    if "maturity_date" in request.json:
          current_isin["maturity_date"] = request.json["maturity_date"]
    if "issuer_name" in request.json:
          current_isin["issuer_name"] = request.json["issuer_name"]      
    if "coupon_rate" in request.json:
          current_isin["coupon_rate"] = request.json["coupon_rate"]      
    if "denomination" in request.json:
          current_isin["denomination"] = request.json["denomination"]      
    return jsonify(current_isin)

# delete isin
@app.route('/isins/<isin_code>', methods = ['DELETE'])
def delete_isin(isin_code): 
    found_isins = list(filter(lambda t : t['isin_code'] == isin_code, isins))
    if len(found_isins) == 0:
          return jsonify({}), 404
    isins.remove(found_isins[0])      
    return jsonify({"done": True})


if __name__ == '__main__':
   app.run(debug=True)


