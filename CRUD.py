from sqlalchemy.orm import Session
import models, schemas

# PartRecord CRUD
def create_part_record(db: Session, part_record: schemas.PartRecordCreate):
    db_part_record = models.PartRecord(**part_record.dict())
    db.add(db_part_record)
    db.commit()
    db.refresh(db_part_record)
    return db_part_record

def get_part_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PartRecord).offset(skip).limit(limit).all()

# BillsOfMaterials CRUD
def create_bills_of_materials(db: Session, bom: schemas.BillsOfMaterialsCreate):
    db_bom = models.BillsOfMaterials(**bom.dict())
    db.add(db_bom)
    db.commit()
    db.refresh(db_bom)
    return db_bom

def get_bills_of_materials(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.BillsOfMaterials).offset(skip).limit(limit).all()

# Order CRUD
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Orders(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Orders).offset(skip).limit(limit).all()

# Inventory CRUD
def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def get_inventory(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Inventory).offset(skip).limit(limit).all()

# Routing CRUD
def create_routing(db: Session, routing: schemas.RoutingCreate):
    db_routing = models.Routing(**routing.dict())
    db.add(db_routing)
    db.commit()
    db.refresh(db_routing)
    return db_routing

def get_routing(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Routing).offset(skip).limit(limit).all()

# Workcenter CRUD
def create_workcenter(db: Session, workcenter: schemas.WorkcenterCreate):
    db_workcenter = models.Workcenter(**workcenter.dict())
    db.add(db_workcenter)
    db.commit()
    db.refresh(db_workcenter)
    return db_workcenter

def get_workcenters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Workcenter).offset(skip).limit(limit).all()
