from flask import Flask, jsonify
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/hello')
def index_api():
    return jsonify({'message': 'Hello, world'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
