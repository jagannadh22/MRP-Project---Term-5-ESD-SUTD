from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import crud
from database import SessionLocal, engine
from mrp_logic import calculate_mrp

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/mrp/")
def run_mrp(db: Session = Depends(get_db)):
    results = calculate_mrp(db)
    return results

# Part Records Endpoints
@app.post("/part_records/", response_model=schemas.PartRecord)
def create_part_record(part_record: schemas.PartRecordCreate, db: Session = Depends(get_db)):
    return crud.create_part_record(db=db, part_record=part_record)

@app.get("/part_records/", response_model=List[schemas.PartRecord])
def read_part_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_part_records(db, skip=skip, limit=limit)

# Bills of Materials Endpoints
@app.post("/bills_of_materials/", response_model=schemas.BillsOfMaterials)
def create_bills_of_materials(bom: schemas.BillsOfMaterialsCreate, db: Session = Depends(get_db)):
    return crud.create_bills_of_materials(db=db, bom=bom)

@app.get("/bills_of_materials/", response_model=List[schemas.BillsOfMaterials])
def read_bills_of_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_bills_of_materials(db, skip=skip, limit=limit)

# Orders Endpoints
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@app.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)

# Inventory Endpoints
@app.post("/inventory/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db=db, inventory=inventory)

@app.get("/inventory/", response_model=List[schemas.Inventory])
def read_inventory(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_inventory(db, skip=skip, limit=limit)

# Routing Endpoints
@app.post("/routing/", response_model=schemas.Routing)
def create_routing(routing: schemas.RoutingCreate, db: Session = Depends(get_db)):
    return crud.create_routing(db=db, routing=routing)

@app.get("/routing/", response_model=List[schemas.Routing])
def read_routing(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_routing(db, skip=skip, limit=limit)

# Workcenter Endpoints
@app.post("/workcenters/", response_model=schemas.Workcenter)
def create_workcenter(workcenter: schemas.WorkcenterCreate, db: Session = Depends(get_db)):
    return crud.create_workcenter(db=db, workcenter=workcenter)

@app.get("/workcenters/", response_model=List[schemas.Workcenter])
def read_workcenters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_workcenters(db, skip=skip, limit=limit)
