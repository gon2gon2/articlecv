from flask import Flask, render_template

def create_app():

    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def root():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=80)