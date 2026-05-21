from fastapi import HTTPException
import pytest

from app.services import form as service
from app.models.enum import Status as EnumStatus

class TestFormServices:

    def test_create_form_200(self, repo, valid_form_data):
        result = service.create_form(valid_form_data, repo)
        assert result.status == EnumStatus.PENDING


    def test_create_form_400(self, repo, valid_form_data):
        service.create_form(valid_form_data, repo)
        with pytest.raises(HTTPException) as exc:
            service.create_form(valid_form_data, repo)
        assert exc.value.status_code == 400