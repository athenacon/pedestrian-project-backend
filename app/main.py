import pymysql
import datetime
import uvicorn as uvicorn
import json
from zoneinfo import ZoneInfo
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware


class TestResults(BaseModel):
    test_name: str
    test_key: float = None

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
    test_key_questionnaire: float = None

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
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.post("/mock_post_test_results/")
async def mock_post_test_results(test_results: TestResults):
    submit_time = datetime.datetime.now(tz=ZoneInfo("Europe/Nicosia"))

    print(submit_time, "submit on mock_post_test_results!")

    res_file_path = Path(
        Path.cwd(),
        "submitted",
        f"test_res_{submit_time.strftime('%Y%m%d_%H%M%S')}.json",
    )
    res_file_path.parent.mkdir(parents=True, exist_ok=True)
        
    res_dir = Path(Path.cwd(), "submitted")
    number_of_files = len(list(res_dir.glob("*.json")))
    test_results.test_key = number_of_files/2

    with res_file_path.open("w") as f:
        f.write(test_results.json(indent=2))

@app.post("/post_quest_res/")
async def post_quest_res(questionnaire_results: Questionnaire):
    submit_time = datetime.datetime.now(tz=ZoneInfo("Europe/Nicosia"))

    print(submit_time, "submit on mock_post_test_results!")

    res_file_path = Path(
        Path.cwd(),
        "submitted",
        f"quest_res_{submit_time.strftime('%Y%m%d_%H%M%S')}.json",
    )
    res_file_path.parent.mkdir(parents=True, exist_ok=True)
        
    res_dir = Path(Path.cwd(), "submitted")
    number_of_files = len(list(res_dir.glob("*.json"))) -1
    questionnaire_results.test_key_questionnaire = number_of_files
    
    with res_file_path.open("w") as f:
        f.write(questionnaire_results.json(indent=2))

@app.get("/")
async def root():
    res_dir = Path(Path.cwd(), "submitted")
    res_dir.mkdir(parents=True, exist_ok=True)
    submitted = list(res_dir.glob("*.json"))
    return {"message": "Pedestrian project backend :)", "submitted": submitted}


@app.get("/download_all_submitted/")
async def download_all_submitted():
    res_dir = Path(Path.cwd(), "submitted")
    res_dir.mkdir(parents=True, exist_ok=True)
    all_res = []
    for submitted in res_dir.glob("*.json"):
        with submitted.open("r") as f: {
            all_res.append(json.load(f),'\n')
             
            
    return {"message": "Pedestrian project backend :)", "submitted": all_res}

if __name__ == "__main__":
    uvicorn.run("main:app")
