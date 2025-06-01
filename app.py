from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', page='home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you would process/save/send the message, for now just print
        print(f"Message from {name} ({email}): {message}")
        success = True
    return render_template('index.html', page='contact', success=success)

if __name__ == '__main__':
    app.run(debug=True)
