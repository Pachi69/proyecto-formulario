

class TestAdminRoutes:

    def test_get_by_id_200(self, client, valid_form_request, mock_form, mocker):
        mocker.patch("app.routes.admin.service.get_by_id", return_value=mock_form)
        client.post("/form", json=valid_form_request)
        response = client.get("/admin/forms/1")

        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_get_by_id_404(self, client, valid_form_request, mocker):
        mocker.patch("app.routes.admin.service.get_by_id", return_value= None)
        client.post("/form", json=valid_form_request)
        response = client.get("/admin/forms/2")

        assert response.status_code == 404

    def test_get_all_by_status_200(self, client, valid_form_request, valid_form_request2, mock_form, mock_form2, mocker):
        mocker.patch("app.routes.admin.service.get_all_by_status", return_value=[mock_form, mock_form2])
        client.post("/form", json=valid_form_request)
        client.post("/form", json=valid_form_request2)

        response = client.get("/admin/forms?status_filter=Pending")

        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_get_all_by_status_204(self, client, valid_form_request, mocker):
        mocker.patch("app.routes.admin.service.get_all_by_status", return_value=[])
        client.post("/form", json=valid_form_request)

        response = client.get("/admin/forms?status_filter=Rejected")

        assert response.status_code == 204

    def test_get_all_by_status_404(self, client, mocker):
        mocker.patch("app.routes.admin.service.get_all", return_value=None)

        response = client.get("/admin/forms")

        assert response.status_code == 404

    def test_accepted_200(self, client, valid_form_request, mock_form_accepted, mocker):
        mocker.patch("app.routes.admin.service.update_status", return_value=mock_form_accepted)
        client.post("/form", json=valid_form_request)
        response = client.patch("/admin/forms/1/approve", json={"status": "Accepted"})

        assert response.status_code == 200
        assert response.json()["status"] == "Accepted"
    
    def test_accepted_404(self, client, valid_form_request, mocker):
        mocker.patch("app.routes.admin.service.update_status", return_value=None)
        client.post("/form", json=valid_form_request)
        response = client.patch("/admin/forms/2/approve", json={"status": "Accepted"})

        assert response.status_code == 404

    def test_accepted_400(self, client, valid_form_request, mocker):
        mocker.patch("app.routes.admin.service.update_status", return_value=None)
        client.post("/form", json=valid_form_request)
        response = client.patch("/admin/forms/2/approve", json={"status": "Approved"})

        assert response.status_code == 400