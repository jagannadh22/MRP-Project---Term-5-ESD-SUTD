from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class PartRecord(Base):
    __tablename__ = "part_records"
    part_id = Column(Integer, primary_key=True, index=True)
    part_name = Column(String, index=True)
    description = Column(String, index=True)

class BillsOfMaterials(Base):
    __tablename__ = "bills_of_materials"
    bom_id = Column(Integer, primary_key=True, index=True)
    parent_part_id = Column(Integer, ForeignKey('part_records.part_id'))
    child_part_id = Column(Integer, ForeignKey('part_records.part_id'))
    quantity = Column(Integer)

class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    part_id = Column(Integer, ForeignKey('part_records.part_id'))
    quantity = Column(Integer)
    order_date = Column(String)

class Inventory(Base):
    __tablename__ = "inventory"
    part_id = Column(Integer, ForeignKey('part_records.part_id'), primary_key=True)
    quantity = Column(Integer)

class Routing(Base):
    __tablename__ = "routing"
    routing_id = Column(Integer, primary_key=True, index=True)
    part_id = Column(Integer, ForeignKey('part_records.part_id'))
    workcenter_id = Column(Integer, ForeignKey('workcenters.workcenter_id'))
    sequence = Column(Integer)

class Workcenter(Base):
    __tablename__ = "workcenters"
    workcenter_id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
