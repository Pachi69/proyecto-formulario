

class TestForm:
    
    def test_create_204(self, client, valid_form_request, mocker):
        mocker.patch("app.routers.form.services.create_form")
        response = client.post("/form", json=valid_form_request)
        assert response.status_code == 204
    
    def test_create_400(self, client, invalid_form_request):
        response = client.post("/form", json=invalid_form_request)
        assert response.status_code == 400

    def test_get_form_by_email_200(self, client, valid_form_request):
        response = client.post("/form", json=valid_form_request)
        response = client.get("/form/user/tupu@tamadre.com")
        assert response.status_code == 200
        assert response.json()["status"] == "Pending"
        assert response.json()["email"] == "tupu@tamadre.com"
        assert response.json()["id"] == 1

    def test_get_form_by_email_404(self, client, valid_form_request):
        client.post("/form", json=valid_form_request)
        response_get = client.get("/form/user/tupu@t.com")
        assert response_get.status_code == 404

    def test_upload_file_200(self, client):
        file = {
            "image": ("file.jpg", b"file content", "image/jpeg")
        }

        response = client.post("/form/attachment", files=file)
        assert response.status_code == 200
        assert response.json() == "https://fake-url.com/file.jpg"
    
    def test_upload_file_400(self, client):
        file = {
            "image": ("file.jpg", b"file content", "image/gif")
        }

        response = client.post("/form/attachment", files=file)
        assert response.status_code == 400
