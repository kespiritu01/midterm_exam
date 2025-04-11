from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('contact_form.html')

@app.route('/confirmation', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone_number']
        message = request.form['message']

        return render_template('confirmation.html', name=name, email=email, phone=phone, message=message)

if __name__ == '__main__':
    app.run()