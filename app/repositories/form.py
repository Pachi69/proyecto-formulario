from sqlalchemy.orm import Session

from app.models.form import FormModel
from app.schemas.form import FormRequest, FormApproval

class FormRepository:
    def __init__(self, db: Session):
        self.db = db


    def create(self, form_data: FormRequest) -> FormModel:
        new_form = FormModel(**form_data.model_dump())

        self.db.add(new_form)
        self.db.commit()
        self.db.refresh(new_form)

        return new_form
    
    def get(self, form_id: int) -> FormModel | None:
        return self.db.query(FormModel).filter(FormModel.id == form_id).first()
    
    def get_by_email(self, email: str) -> FormModel | None:
        return self.db.query(FormModel).filter(FormModel.email == email).first()
    
    def list(self) -> list[FormModel]:
        return self.db.query(FormModel).all()
    
    def update_status(self, form_id: int, approval: FormApproval) -> FormModel | None:
        form = self.get(form_id)

        if form is None:
            return None
       
        form.status = approval.status
        self.db.commit()
        self.db.refresh(form)

        return form
        
       