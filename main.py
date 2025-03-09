from fastapi import FastAPI, Query, HTTPException, Depends
from sqlalchemy.orm import Session, aliased
from sqlalchemy import not_, func, desc
from database import SessionLocal
from models import User, Video, UserInteraction

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/feed")
def get_personalized_feed(
    username: str = Query(...),
    category_id: int = Query(None),  
    db: Session = Depends(get_db)
):
    
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_interactions = db.query(UserInteraction.video_id).filter(UserInteraction.user_id == user.id).subquery()

    video_query = db.query(Video).filter(Video.id.notin_(user_interactions))

    if category_id:
        video_query = video_query.filter(Video.category_id == category_id)

    recommended_videos = video_query.order_by(func.random()).limit(5).all()

    if not recommended_videos:
        recommended_videos = (
            db.query(Video)
            .order_by(desc(Video.id))  
            .limit(5)
            .all()
        )
    return {
        "user": username,
        "recommended_videos": [
            {"id": video.id, "title": video.title, "category_id": video.category_id, "url": video.url}
            for video in recommended_videos
        ],
    }
