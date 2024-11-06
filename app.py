from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_nums():
    nums = request.json #translating my data
    return jsonify({'result': nums['num1'] + nums['num2']}), 200 #returning the result



if __name__ == '__main__':
    app.run(debug=True)