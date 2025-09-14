from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.schemas.item as item_schema
import app.models.item as item_model
from app.api import deps

router = APIRouter()


@router.post("/", response_model=item_schema.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: item_schema.ItemCreate,
):
    """
    Create a new todo item.
    """
    db_item = item_model.Item(title=item_in.title, description=item_in.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# @router.get("/{title}", response_model=item_schema.Item)
# def read_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     title: str,
# ):
#     """
#     Get a specific todo item.
#     """
#     db_item = db.query(item_model.Item).filter(item_model.Item.title == title).first()
#     return db_item