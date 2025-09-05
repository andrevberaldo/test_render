from fastapi import FastAPI

api = FastAPI(
    title="api to test the render platform"
)

@api.get("/hello")
def say_hello():
    return {
        "msg": "render!"
    }