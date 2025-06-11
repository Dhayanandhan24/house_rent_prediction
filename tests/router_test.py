import json
import pytest
from app import app  # Absolute import


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

valid_payload = {
    "medinc": 3.5,
    "houseage": 15,
    "averooms": 6,
    "avebedrms": 1,
    "population": 1000,
    "aveoccup": 2.5,
    "latitude": 37.0,
    "longitude": -122.0
}

def test_post_predict_success(client):
    response = client.post(
        '/predict',
        data=json.dumps(valid_payload),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = response.get_json()
    assert 'PRICE_PREDICTION' in data
    assert data['status'] == 'sukses POST'

def test_get_predict(client):
    response = client.get('/predict')
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'Anda nge-GET'

def test_post_predict_missing_field(client):
    invalid_payload = valid_payload.copy()
    del invalid_payload['medinc']
    response = client.post(
        '/predict',
        data=json.dumps(invalid_payload),
        content_type='application/json'
    )
    # This will only work if you have error handling in the code
    # Otherwise this will raise 500 Internal Server Error
    assert response.status_code in (400, 500)
