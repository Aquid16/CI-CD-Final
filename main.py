from flask import Flask

app = Flask(__name__)


@app.route("/")
def print_this():
    return "This was made by Ansible and Jenkins"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
