from pydantic import BaseModel
from typing import Optional

class PartRecordBase(BaseModel):
    part_name: str
    description: str

class PartRecordCreate(PartRecordBase):
    pass

class PartRecord(PartRecordBase):
    part_id: int

    class Config:
        orm_mode = True

class BillsOfMaterialsBase(BaseModel):
    parent_part_id: int
    child_part_id: int
    quantity: int

class BillsOfMaterialsCreate(BillsOfMaterialsBase):
    pass

class BillsOfMaterials(BillsOfMaterialsBase):
    bom_id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    part_id: int
    quantity: int
    order_date: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    order_id: int

    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    part_id: int
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    pass

    class Config:
        orm_mode = True

class RoutingBase(BaseModel):
    part_id: int
    workcenter_id: int
    sequence: int

class RoutingCreate(RoutingBase):
    pass

class Routing(RoutingBase):
    routing_id: int

    class Config:
        orm_mode = True

class WorkcenterBase(BaseModel):
    location: str

class WorkcenterCreate(WorkcenterBase):
    pass

class Workcenter(WorkcenterBase):
    workcenter_id: int

    class Config:
        orm_mode = True
