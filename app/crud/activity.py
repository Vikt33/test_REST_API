from sqlalchemy.orm import Session
from app.models import Activity

def get_activity(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()

def get_activity_tree(db: Session, parent_id: int = None, depth: int = 0, max_depth: int = 3):
    if depth >= max_depth:
        return []
    query = db.query(Activity)
    if parent_id is None:
        query = query.filter(Activity.parent_id.is_(None))
    else:
        query = query.filter(Activity.parent_id == parent_id)
    activities = query.all()
    for activity in activities:
        activity.children = get_activity_tree(db, activity.id, depth + 1, max_depth)
    return activities