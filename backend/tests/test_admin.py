

class TestAdmin:

    def test_get_by_id_200(self, client, valid_form_request):
        client.post("/form", json=valid_form_request)
        response = client.get("/admin/forms/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_get_by_id_404(self, client, valid_form_request):
        client.post("/form", json=valid_form_request)
        response = client.get("/admin/forms/2")
        assert response.status_code == 404

    def test_get_all_by_status_200(self, client, valid_form_request, valid_form_request2):
        client.post("/form", json=valid_form_request)
        client.post("/form", json=valid_form_request2)

        response = client.get("/admin/forms?status_filter=Pending")
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_get_all_by_status_204(self, client, valid_form_request):
        client.post("/form", json=valid_form_request)

        response = client.get("/admin/forms?status_filter=Rejected")
        assert response.status_code == 204
        
    def test_get_all_by_status_404(self, client):

        response = client.get("/admin/forms")
        assert response.status_code == 404

    def test_approve_200(self, client, valid_form_request):
        client.post("/form", json=valid_form_request)
        response = client.patch("/admin/forms/1/approve", json={"status": "Accepted"})
        assert response.status_code == 200
        assert response.json()["status"] == "Accepted"

    def test_approve_404(self, client, valid_form_request):
        client.post("/form", json=valid_form_request)
        response = client.patch("/admin/forms/2/approve", json={"status": "Accepted"})
        assert response.status_code == 404

    def test_approve_400(self, client, valid_form_request):
        client.post("/form", json=valid_form_request)
        response = client.patch("/admin/forms/1/approve", json={"status": "Approved"})
        assert response.status_code == 400