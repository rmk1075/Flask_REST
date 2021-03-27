# from flask import Flask, jsonify
#
#
# def create_app():
#     app = Flask(__name__)
#
#     @app.route('/hello')
#     def hello():
#         return 'hello'
#
#     @app.route('/json/list')
#     def json_list():
#         data = [1, 2, 3, 4]
#         return jsonify(data)
#
#     @app.route('/json/dict')
#     def json_dict():
#         data = {'a': 1, 'b': 2}
#         return jsonify(data)
#
#     @app.route('/json/string')
#     def json_string():
#         data = '{a:1, b:2}'
#         return jsonify(data)
#
#     return app
