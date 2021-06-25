from flask import Flask


"""
    애플리케이션 팩토리는 쉽게 말해 app 객체를 생성하는 함수를 의미한다.
    create_app 함수가 애플리케이션 팩토리다
    함수명으로 create_app 대신 다른 이름을 사용하면 정상으로 동작하지 않는다. create_app은 플라스크 내부에서 정의된 함수명이다.
"""
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app