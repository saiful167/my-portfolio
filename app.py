from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "bd"
API_URL = "https://helobuy.shop/csms.php"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_sms', methods=['POST'])
def send_sms():
    numbers = request.form['numbers'].split(",")
    amount = request.form['amount']
    success = 0
    fail = 0

    for num in numbers:
        message = f"আপনার অ্যাকাউন্টে {amount} টাকা যুক্ত হয়েছে।"
        payload = {
            'key': API_KEY,
            'number': num.strip(),
            'message': message
        }
        try:
            r = requests.get(API_URL, params=payload)
            if "success" in r.text.lower():
                success += 1
            else:
                fail += 1
        except Exception as e:
            fail += 1

    return render_template("index.html", response=f"{success} SMS সফল, {fail} ব্যর্থ।")

if __name__ == '__main__':
    app.run(debug=True)
