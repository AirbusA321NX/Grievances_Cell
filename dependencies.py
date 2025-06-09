from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from User import models as user_models
from roles import RoleEnum

# Dummy Auth — Replace with JWT in real case
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = ""):
    # Simulate token-to-user mapping
    # Replace with JWT decode logic in real app
    user = db.query(user_models.User).filter(user_models.User.email == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user token")
    return user

# Role check dependencies
def require_role(required_roles: list[RoleEnum]):
    def role_checker(current_user: user_models.User = Depends(get_current_user)):
        if current_user.role not in required_roles:
            raise HTTPException(status_code=403, detail="Forbidden: insufficient role")
        return current_user
    return role_checker
