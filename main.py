import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class TestResults(BaseModel):
    test_name: str

    test_1: str = None
    test_2: str = None
    test_3: str = None
    test_4: str = None
    test_5: str = None
    test_6: str = None
    test_7: str = None
    test_8: str = None
    test_9: str = None
    test_10: str = None

    test_1_reaction_time: float = None
    test_2_reaction_time: float = None
    test_3_reaction_time: float = None
    test_4_reaction_time: float = None
    test_5_reaction_time: float = None
    test_6_reaction_time: float = None
    test_7_reaction_time: float = None
    test_8_reaction_time: float = None
    test_9_reaction_time: float = None
    test_10_reaction_time: float = None


app = FastAPI()


@app.post("/post_test_results/")
async def post_test_results(test_results: TestResults):
    print(test_results)


@app.get("/")
async def root():
    return {"message": "Pedestrian project backend :)"}


if __name__ == "__main__":
    uvicorn.run("main:app")
