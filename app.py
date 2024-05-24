import os
from flask import Flask, jsonify, request, render_template, flash
from Tami4 import ApiKey, Tami4Handler, Tami4KeyHandler
app = Flask(__name__)
app.secret_key = 'super secret key'

## Check for Tami4Edge API Key Configuration
if ApiKey.API_KEY == '':
    print('''WARNING!!
No Api Key configured. 
Point your browser to http://<host_ip>:<port>/site/tami4setup and follow the instructions')
''')
    
@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/site/tami4setup', methods=['GET','POST'])
def tami4setup():
    active_page = 'tami4setup'
    if request.method == 'GET':
        return render_template('tami_form.html', active_page=active_page)
    
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
    if ApiKey.API_KEY == '':
        return jsonify(error='No Api Key configured. Point your browser to http://<host_ip>:<port>/site/tami4setup and follow the instructions'), 500
    try:
        # Assuming tami4_actions.boil_water() may raise exceptions on error
        Tami4Handler.boil_water()
        print("Tami4: Boil - Command sent successfully.")
        return jsonify(message='Boil Water command sent successfully.'), 200  # 200 OK for success
    except Exception as e:
        # You can customize the error message and status code based on the exception
        print(str(e))
        return jsonify(error=str(e)), 500  # 500 Internal Server Error for generic errors


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
