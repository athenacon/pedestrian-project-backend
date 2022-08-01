import pymysql
import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware


class TestResults(BaseModel):
    test_name: str

    test_a_1: str = None
    test_a_2: str = None
    test_a_3: str = None
    test_a_4: str = None
    test_a_5: str = None
    test_a_6: str = None
    test_a_7: str = None
    test_a_8: str = None
    test_a_9: str = None
    test_a_10: str = None

    test_a_1_reaction_time: float = None
    test_a_2_reaction_time: float = None
    test_a_3_reaction_time: float = None
    test_a_4_reaction_time: float = None
    test_a_5_reaction_time: float = None
    test_a_6_reaction_time: float = None
    test_a_7_reaction_time: float = None
    test_a_8_reaction_time: float = None
    test_a_9_reaction_time: float = None
    test_a_10_reaction_time: float = None

    test_b_1: str = None
    test_b_2: str = None
    test_b_3: str = None
    test_b_4: str = None
    test_b_5: str = None
    test_b_6: str = None
    test_b_7: str = None
    test_b_8: str = None
    test_b_9: str = None
    test_b_10: str = None

    test_b_1_reaction_time: float = None
    test_b_2_reaction_time: float = None
    test_b_3_reaction_time: float = None
    test_b_4_reaction_time: float = None
    test_b_5_reaction_time: float = None
    test_b_6_reaction_time: float = None
    test_b_7_reaction_time: float = None
    test_b_8_reaction_time: float = None
    test_b_9_reaction_time: float = None
    test_b_10_reaction_time: float = None


class Questionnaire(BaseModel):
    test_name: str

    gender: str = None
    age_range: str = None
    familiarity_tech: str = None

    myRange1: int = None
    myRange2: int = None
    myRange3: int = None
    myRange4: int = None
    myRange5: int = None
    myRange6: int = None
    myRange7: int = None
    myRange8: int = None
    myRange9: int = None
    myRange10: int = None
    text_box: str = None


app = FastAPI()

origins = ["https://athenacon.github.io"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
    res.setHeader('Access-Control-Allow-Credentials', true);
    // handle OPTIONS method
    if ('OPTIONS' == req.method) {
        return res.sendStatus(200);
    } else {
        next();
    }
});

@app.post("/mock_post_test_results/")
async def mock_post_test_results(test_results: TestResults):
    print("test A")
    return {"message": "Moch post test results"}

    
@app.get("/")
async def root():
    return {"message": "Pedestrian project backend :)"}


if __name__ == "__main__":
    uvicorn.run("main:app")
