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

@router.get("/{item_id}", response_model=item_schema.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
):
    """
    Get an item by its ID.
    """
    item = db.query(item_model.Item).filter(item_model.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=list[item_schema.Item])
def read_items(
    *, db: Session = Depends(deps.get_db)
):
    """
    Retrieve all items.
    """
    items = db.query(item_model.Item).all()
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items

@router.put("/{item_id}", response_model=item_schema.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    item_in: item_schema.ItemUpdate,
):
    """
    Update an item by its ID.
    """
    item = db.query(item_model.Item).filter(item_model.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.title = item_in.title
    item.description = item_in.description
    item.completed = item_in.completed
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}", response_model=item_schema.Item)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
):
    """
    Delete an item by its ID.
    """
    item = db.query(item_model.Item).filter(item_model.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return item