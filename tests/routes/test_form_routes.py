from fastapi import HTTPException
import pytest


class TestFormRoutes:

    def test_create_form_204(self, client, valid_form_request, mocker):
        mocker.patch("app.routes.form.service.create_form")
        response = client.post("/form", json=valid_form_request)
        assert response.status_code == 204


    def test_get_form_by_email_200(self, client, mock_form, mocker):
        mocker.patch("app.routes.form.service.get_form_by_email", return_value=mock_form)
        response = client.get("/form/user/tupu@tamadre.com")
        assert response.status_code == 200
        assert response.json()["email"] == "tupu@tamadre.com"
        assert response.json()["status"] == "Pending"