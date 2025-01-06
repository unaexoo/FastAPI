from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import questioin_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)

@router.get("/list", response_model=list[questioin_schema.Question])
def questioin_list(db : Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

