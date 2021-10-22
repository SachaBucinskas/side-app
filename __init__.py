from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test/')
def alternate_page():
    return 'Different page, different text, same website!'

@app.route('/test/<int:test_number>/')
def test_page_number(test_number):
    return f'This is a test page that passes in a variable from the URL, which is {test_number}'

if __name__ == '__main__':
    app.run(debug=True) 