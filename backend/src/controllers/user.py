from fastapi import APIRouter


users_route = APIRouter(tags=["users"])

# TODO get APIResponse model


@users_route.get("/all-users")
def get_users():

    return
