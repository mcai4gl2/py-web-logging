def test_ping(app):
    response = app.get('/api/v1.0/ping')
    assert response.status_code == 200
