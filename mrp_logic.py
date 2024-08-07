from sqlalchemy.orm import Session
import models

def calculate_mrp(db: Session):
    parts = db.query(models.PartRecord).all()
    boms = db.query(models.BillsOfMaterials).all()
    inventory = db.query(models.Inventory).all()  # Assume an Inventory table exists
    orders = db.query(models.Orders).all()
    
    mrp_results = []

    for part in parts:
        gross_requirements = sum(order.quantity for order in orders if order.part_id == part.part_id)
        scheduled_receipts = 0  # This should be fetched from another source if available
        on_hand_inventory = next((inv.quantity for inv in inventory if inv.part_id == part.part_id), 0)
        net_requirements = gross_requirements - on_hand_inventory - scheduled_receipts
        planned_order_releases = max(net_requirements, 0)

        mrp_results.append({
            "part_id": part.part_id,
            "gross_requirements": gross_requirements,
            "scheduled_receipts": scheduled_receipts,
            "on_hand_inventory": on_hand_inventory,
            "net_requirements": net_requirements,
            "planned_order_releases": planned_order_releases
        })
    
    return mrp_results
