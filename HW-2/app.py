from flask import Flask
from flask import make_response
from flask import request
from flask import json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

localStorage = dict()

CODE_OK = 200
CODE_BAD_REQUEST = 400
CODE_BAD_KEY = 404
CODE_BAD_METHOD = 405
CODE_BAD_MEDIA = 415

TYPE_PLAIN = 'text/plain'
TYPE_JSON = 'application/json'

# helper functions

def response_with(code):
    response = make_response()
    response.status_code = code
    return response

# handler functions

@app.get('/hello')
def hello():
    response = make_response('HSE One Love!', CODE_OK)
    response.content_type = TYPE_PLAIN
    return response

@app.get('/get/<key>')
def get_key(key):
    if key not in localStorage:
        return response_with(CODE_BAD_KEY)

    return app.response_class(
        response = json.dumps(
            {
                'key': key,
                'value': localStorage[key]
            }
        ),
        status = CODE_OK,
        content_type = TYPE_JSON
    )

@app.post('/set')
def set_key():
    if not request.content_type == TYPE_JSON:
        return response_with(CODE_BAD_MEDIA)
    
    content = request.get_json()
    if not ('key' in content and 'value' in content):
        return response_with(CODE_BAD_REQUEST)
    
    localStorage[content['key']] = content['value']
    return response_with(CODE_OK)
    
@app.post('/divide')
def divide():

    if not request.content_type == TYPE_JSON:
        return response_with(CODE_BAD_MEDIA)

    content = request.get_json()
    if not ('dividend' in content and 'divider' in content):
        return response_with(CODE_BAD_REQUEST)

    dividend = content['dividend']
    divider = content['divider']

    if divider == 0:
        return response_with(CODE_BAD_REQUEST)

    response = response_with(CODE_OK)
    response.content_type = TYPE_PLAIN
    response.set_data(str(dividend / divider))
    return response

@app.errorhandler(HTTPException)
def handle_exception(e):
    return response_with(CODE_BAD_METHOD)

if __name__ == '__main__':
    app.run()