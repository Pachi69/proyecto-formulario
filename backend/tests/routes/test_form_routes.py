from fastapi import HTTPException
import pytest


class TestFormRoutes:

    def test_create_form_204(self, client, valid_form_request, mocker):
        mocker.patch("app.routes.form.service.create_form")
        response = client.post("/form", json=valid_form_request)
        assert response.status_code == 204

    def test_create_form_400(self, client, invalid_form_request, mocker):
        mocker.patch("app.routes.form.service.create_form")
        response = client.post("/form", json=invalid_form_request)
        assert response.status_code == 400


    def test_get_form_by_email_200(self, client, mock_form, mocker):
        mocker.patch("app.routes.form.service.get_form_by_email", return_value=mock_form)
        response = client.get("/form/user/tupu@tamadre.com")
        assert response.status_code == 200
        assert response.json()["email"] == "tupu@tamadre.com"
        assert response.json()["status"] == "Pending"
        assert response.json()["id"] == 1

    def test_get_form_by_email_404(self, client, mocker):
        mocker.patch("app.routes.form.service.get_form_by_email", return_value=None)
        response = client.get("/form/user/tupu@t.com")
        assert response.status_code == 404

    def test_upload_attachment_200(self, client, mock_fake_url, mocker):
        mocker.patch("app.routes.form.service.upload_attachment", return_value=mock_fake_url)
        file = {"image": ("file.jpg", b"file content", "image/jpeg")}

        response = client.post("/form/attachment", files=file)
        assert response.status_code == 200
        assert response.json() == mock_fake_url

    def test_upload_attachment_400(self, client, mocker):
        mocker.patch("app.routes.form.service.upload_attachment")
        file = {"image": ("file.jpg", b"file content", "image/gif")}

        response = client.post("/form/attachment", files=file)
        assert response.status_code == 400



