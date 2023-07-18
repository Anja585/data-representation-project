# Module: Data representation
# Author: Anja Antolkovic


from flask import Flask, jsonify, request, abort, render_template
from dao import isinDAO


app = Flask(__name__, static_url_path='', static_folder='static', template_folder="static")

@app.route('/')
def hello(): 
    return render_template('/ea.html')

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
    if not request.form: 
          abort(400)
    new_isin = {
          "isin_code" : request.form["isin_code"], 
          "issuance_date" : request.form["issuance_date"],
          "maturity_date" : request.form["maturity_date"],
          "coupon_rate" : request.form["coupon_rate"],
          "denomination" : request.form["denomination"]
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
    found_isin = list(isinDAO.find_isin(isin_code)[0])
    if not found_isin:
          abort(404)
    if not request.form:
         abort(404)
    if "issuance_date" in request.form:
          found_isin[1] = request.form["issuance_date"]
    if "maturity_date" in request.form:
          found_isin[2] = request.form["maturity_date"]
    if "denomination" in request.form:
          found_isin[4] = request.form["denomination"]
    if "coupon_rate" in request.form:
          found_isin[3] = request.form["coupon_rate"]                  
    values = (found_isin[1],
              found_isin[2],
              found_isin[3],
              found_isin[4],
              found_isin[0])
    isinDAO.update(values)
    return jsonify(found_isin)

# delete isin
@app.route('/isins/<isin_code>', methods = ['DELETE'])
def delete_isin(isin_code): 
    isinDAO.delete(isin_code)
    return jsonify({"done": True})


if __name__ == '__main__':
   app.run(debug=True)


