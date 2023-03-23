from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/guestbook')
def main():
   return render_template('guestbook.html')


@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST 연결 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
