from fastapi import HTTPException, Depends
import pytest

from app.services import form as service
from app.models.enum import Status as EnumStatus
from app.storage.fake_storage import FakeStorage

class TestFormServices:

    def test_create_form(self, repo, valid_form_data):
        result = service.create_form(valid_form_data, repo)
        assert result.status == EnumStatus.PENDING

    def test_create_form_409(self, repo, valid_form_data):
        service.create_form(valid_form_data, repo)
        with pytest.raises(HTTPException) as exc:
            service.create_form(valid_form_data, repo)
        assert exc.value.status_code == 409

    def test_create_form_unregister_404(self, repo, valid_form_data):
        valid_form_data.form_type = "Unregister"
        with pytest.raises(HTTPException) as exc:
            service.create_form(valid_form_data, repo)
        assert exc.value.status_code == 404

    def test_get_form_by_email(self, repo, valid_form_data):
        service.create_form(valid_form_data, repo)
        result = service.get_form_by_email(valid_form_data.email, repo)
        assert result
        assert result.email == valid_form_data.email

    def test_get_by_id(self, repo, valid_form_data):
        service.create_form(valid_form_data, repo)
        result = service.get_by_id(1, repo)
        assert result
        assert result.id == 1

    def test_get_all_by_status(self, repo, valid_form_data, valid_form_data2, form_accepted):
        service.create_form(valid_form_data, repo)
        service.create_form(valid_form_data2, repo)
        service.update_status(1, form_accepted, repo)

        result = service.get_all_by_status(EnumStatus.PENDING, repo)
        assert result
        assert len(result) == 1
        assert result[0].status == EnumStatus.PENDING

    def test_get_all(self, repo, valid_form_data, valid_form_data2):
        service.create_form(valid_form_data, repo)
        service.create_form(valid_form_data2, repo)

        result = service.get_all(repo)
        assert result
        assert len(result) == 2

    def test_upload_attachment(self):
        file = {"image": ("file.jpg", b"file content", "image/jpeg")}
        storage = FakeStorage()
        result = service.upload_attachment(file, storage)
        assert result
        assert result == "https://fake-url.com/file.jpg"

    def test_update_status(self, repo, valid_form_data, form_accepted):
        service.create_form(valid_form_data, repo)
        result = service.update_status(1, form_accepted, repo)

        assert result
        assert result.status == EnumStatus.ACCEPTED

    def test_update_status_400(self, repo, valid_form_data, invalid_form_accepted):
        service.create_form(valid_form_data, repo)
        with pytest.raises(HTTPException) as exc:
            service.update_status(1, invalid_form_accepted, repo)
        assert exc.value.status_code == 400

    def test_update_status_404(self, form_accepted, repo):
        with pytest.raises(HTTPException) as exc:
            service.update_status(1, form_accepted, repo)
        assert exc.value.status_code == 404
        