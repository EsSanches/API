

from users.schemas import Users

def create_user(user_in: Users):
    user = user_in.model_dump()
    return {"success": True, "user": user}
