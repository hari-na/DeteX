from flask import Flask, json, jsonify, request, make_response
from flask_cors import CORS, cross_origin
import pyotp

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


uName, passW, perms = ['Hari', 'Kavin', 'Tharun'], ['KavuMama', 'TharuMama', 'HaruMama'], ['full', 'half', 'rOnly']



@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    print("Request ongoing")
    CATIDuser = request.args.get("CATID")
    passWuser = request.args.get("passW")
    authGuser = request.args.get("authG")

    if CATIDuser not in uName:
        print("Username not working")
        return jsonify(message = "CAT ID not in Database. Contact Admin", ok = 0)
    else:
        indVal = uName.index(CATIDuser)
        if passWuser != passW[indVal]:
            return jsonify(message = "Incorrect password. To reset, contact Admin", ok = 0)
        else:
            totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
            if authGuser != totp.now():
                return jsonify(message = "Incorrect Authentication OTP. Retry after 30 seconds", ok = 0)
            else:
                print("Logged In")
                return jsonify(message = perms[indVal], ok = 1)

if __name__ == "main":
    app.run(debug=True)