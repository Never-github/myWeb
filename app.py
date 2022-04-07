from flask import Flask
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maishu is fat again, 555'

# @app.route('/')
# def app():  # put application's code here
#     return render_template('base.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
