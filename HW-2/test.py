from app import *

# constants

HEADER_JSON = {
    'Content-Type': 'application/json'
}

HEADER_PLAIN = {
    'Content-Type': 'text/plain'
}

CONTENT_JSON = {
    'key': 'some_key',
    'value': 'some_value'
}

CONTENT_JSON_UPDATE = {
    'key': 'some_key',
    'value': 'another_value'
}

CONTENT_JSON_BAD = {
    'key': 'some_key'
}
    
# helper functions

def setupClient():
    return app.test_client()

def assert_code(response, code):
    assert response.status_code == code

def assert_bad_method(response):
    assert_code(response, CODE_BAD_METHOD)

def assert_plain(response):
    assert response.content_type == TYPE_PLAIN

def assert_json(response):
    assert response.content_type == TYPE_JSON

def assert_text(response, text):
    assert response.get_data(as_text=True) == text

def assert_json_data(response, data):
    assert response.json == data

def test_exception():
    client = setupClient()

    assert_bad_method(client.post('/hello'))
    assert_bad_method(client.put('/hello'))
    assert_bad_method(client.delete('/hello'))

    assert_bad_method(client.get('/set'))
    assert_bad_method(client.put('/set'))
    assert_bad_method(client.delete('/set'))

    assert_bad_method(client.post('/get/key'))
    assert_bad_method(client.put('/get/key'))
    assert_bad_method(client.delete('/get/key'))

    assert_bad_method(client.get('/divide'))
    assert_bad_method(client.put('/divide'))
    assert_bad_method(client.delete('/divide'))

    assert_bad_method(client.get('/wrong_route'))
    assert_bad_method(client.post('/wrong_route'))
    assert_bad_method(client.put('/wrong_route'))
    assert_bad_method(client.delete('/wrong_route'))

def test_hello():
    client = setupClient()

    response = client.get('/hello')

    assert_code(response, CODE_OK)
    assert_plain(response)
    assert_text(response, 'HSE One Love!')

def test_set():

    client = setupClient()

    response = client.post('/set', headers=HEADER_JSON, json=CONTENT_JSON)
    assert_code(response, CODE_OK)

    response = client.post('/set', headers=HEADER_PLAIN)
    assert_code(response, CODE_BAD_MEDIA)

    response = client.post('/set', headers=HEADER_JSON, json={})
    assert_code(response, CODE_BAD_REQUEST)

    response = client.post('/set', headers=HEADER_JSON, json=CONTENT_JSON_BAD)
    assert_code(response, CODE_BAD_REQUEST)

def test_get():

    client = setupClient()

    response = client.post('/set', headers=HEADER_JSON, json=CONTENT_JSON)
    assert_code(response, CODE_OK)
    
    response = client.get('/get/some_key')
    assert_code(response, CODE_OK)
    assert_json(response)
    assert_json_data(response, CONTENT_JSON)

    response = client.post('/set', headers=HEADER_JSON, json=CONTENT_JSON_UPDATE)

    response = client.get('/get/some_key')
    assert_code(response, CODE_OK)
    assert_json(response)
    assert_json_data(response, CONTENT_JSON_UPDATE)

    response = client.get('/get/new_key')
    assert_code(response, CODE_BAD_KEY)


def test_divide():

    client = setupClient()
    
    response = client.post('/divide', headers=HEADER_JSON, 
    json=
        {
            "dividend": 2, "divider": 3
        }
    )
    assert_code(response, CODE_OK)
    assert_plain(response)
    assert_text(response, str(2 / 3))
    
    response = client.post('/divide', headers={})
    assert_code(response, CODE_BAD_MEDIA)
    
    response = client.post('/divide', headers=HEADER_PLAIN)
    assert_code(response, CODE_BAD_MEDIA)

    response = client.post('/divide', headers=HEADER_JSON, json={})
    assert_code(response, CODE_BAD_REQUEST)
    
    response = client.post('/divide', headers=HEADER_JSON, json={"dividend": 2})
    assert_code(response, CODE_BAD_REQUEST)
    
    response = client.post('/divide', headers=HEADER_JSON, json={"divider": 3})
    assert_code(response, CODE_BAD_REQUEST)
    
    response = client.post('/divide', headers=HEADER_JSON, json={"dividend": 1, "divider": 0})
    assert_code(response, CODE_BAD_REQUEST)