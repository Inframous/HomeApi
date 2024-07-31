import os
from flask import Flask, jsonify, request, render_template, flash
from Tami4 import Tami4KeyHandler, Tami4Handler
from Tami4.api_key.ApiKey import API_KEY
app = Flask(__name__)
app.secret_key = 'super secret key'

NO_KEY_ERROR = 'No Api Key configured. Point your browser to http://<host_ip>:<port>/site/tami4setup and follow the instructions'    

## Check for Tami4Edge API Key Configuration
if API_KEY == '':
    print(f'''WARNING!!
No Api Key configured. 
{NO_KEY_ERROR}
''')


@app.route('/')
def hello_world():
    return jsonify(message='Hello World! Point your browser to http://<host_ip>:<port>/site/tami4setup and follow the instructions')

@app.route('/site/tami4setup', methods=['GET','POST'])
def tami4setup():
    active_page = 'tami4setup'
    KEY_OBTAINED = False
    if request.method == 'GET':
        if API_KEY != '':
            KEY_OBTAINED = True
        return render_template('tami_form.html', active_page=active_page, key_obtained=KEY_OBTAINED)
    
    if request.method == 'POST':
        mobile_number = request.form['mobileNumber']
        Tami4KeyHandler.request_key(mobile_number)
        return render_template('tami_form.html', active_page=active_page, mobile_number=mobile_number)

@app.route('/api/tami4/send_otp', methods=['POST'])
def send_otp():
    mobile_number = request.form['mobileNumber']
    otp_code = request.form['otpCode']
    print(f"Mobile: {mobile_number}, OTP:{otp_code}")
    Tami4KeyHandler.send_otp(otp_code, mobile_number)
    flash('Success! API Key configured successfully.')
    return render_template('tami_form.html')


@app.route('/api/tami4/boil', methods=['POST'])
def tami_boil():
    if API_KEY == '':
        return jsonify(error=NO_KEY_ERROR), 500
    try:
        Tami4Handler.boil_water()
        print("Tami4: Boil - Command sent successfully.")
        return jsonify(message='Boil Water command sent successfully.'), 200  
    except Exception as e:
        print(str(e))
        return jsonify(error=str(e)), 500  


@app.route('/api/tami4/get_drinks', methods=['GET'])
def tami_get_drink():
    if API_KEY == '':
        return jsonify(error=NO_KEY_ERROR), 500
    try:
        drinks = Tami4Handler.list_drinks()
        print("Tami4: Get Drinks - Command sent successfully.")
        return jsonify(drinks), 200
    except Exception as e:
        print(str(e))
        return jsonify(error=str(e)), 500  


@app.route('/api/tami4/make/<int:drink_index>', methods=['POST'])
def make_drink(drink_index):
    if API_KEY == '':
        return jsonify(error=NO_KEY_ERROR), 500
    try:
        drink_name = Tami4Handler.make_drink(int(drink_index))
        print(f"Tami4: Prepare Drink ({drink_name}) - Command sent successfully.")
        return jsonify(message=f"Successfully start preparing {drink_name}."), 200  
    except Exception as e:
        print(str(e))
        return jsonify(error=str(e)), 500  
    

@app.route('/api/tami4/info', methods=['GET'])
def get_info():
    if API_KEY == '':
        return jsonify(error=NO_KEY_ERROR), 500
    try:
        info = Tami4Handler.get_tami4_info()
        print("Tami4: Get Info - Command sent successfully.")
        return jsonify(info), 200
    except Exception as e:
        print(str(e))
        return jsonify(error=str(e)), 500  

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
