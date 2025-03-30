from fastapi import HTTPException


def validate_user(user):
    if not user:
        raise HTTPException(status_code=404, detail="User not found")