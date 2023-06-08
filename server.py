# Module: Data representation
# Author: Anja Antolkovic


from flask import Flask, jsonify, request, abort
from dao import isinDAO


app = Flask(__name__, static_url_path='', static_folder='static_pages')

@app.route('/')
def hello(): 
    return 'hello'

# get all
@app.route('/isins', methods = ['GET'])
def get_all_isins():
    results = isinDAO.get_all()     
    return jsonify(results)

# get isin
@app.route('/isins/<isin_code>', methods = ['GET'])
def get_isin(isin_code):
    found_isins = isinDAO.find_isin(isin_code)
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
          "coupon_rate" : request.json["coupon_rate"],
          "denomination" : request.json["denomination"]
           }
    values = (new_isin['isin_code'], 
              new_isin['issuance_date'],
              new_isin['maturity_date'],
              new_isin['coupon_rate'],
              new_isin['denomination'])
    isinDAO.create(values)
    return jsonify(new_isin)

# update isin
@app.route('/isins/<isin_code>', methods = ['PUT'])
def update_isin(isin_code):
    found_isin = isinDAO.find_isin(isin_code)
    if not found_isin:
          abort(404)
    if not request.json:
         abort(404)
    req_json = request.json
    if "coupon_rate" in request.json and type(req_json['coupon_rate']) is not int:
          abort(400)
    if "issuance_date" in req_json:
          found_isin["issuance_date"] = req_json["issuance_date"]
    if "maturity_date" in request.json:
          found_isin["maturity_date"] = req_json["maturity_date"]
    if "denomination" in request.json:
          found_isin["denomination"] = req_json["denomination"]      
    values = (found_isin['isin_code'],
              found_isin['issuance_date'],
              found_isin['maturity_date'],
              found_isin['coupon_rate'],
              found_isin['denomination'])
    isinDAO.update(values)
    return jsonify(found_isin)

# delete isin
@app.route('/isins/<isin_code>', methods = ['DELETE'])
def delete_isin(isin_code): 
    isinDAO.delete(isin_code)
    return jsonify({"done": True})

if __name__ == '__main__':
   app.run(debug=True)


