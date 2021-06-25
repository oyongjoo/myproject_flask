from flask import Flask


# 애플리케이션 팩토리는 쉽게 말해 app 객체를 생성하는 함수를 의미한다.
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app