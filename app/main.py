from datetime import datetime
from zoneinfo import ZoneInfo

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


@app.post("/mock_post_test_results/")
async def mock_post_test_results(test_results: TestResults):
    print(datetime.now(tz=ZoneInfo("Europe/Nicosia")), test_results)


@app.post("/post_test_results/")
async def post_test_results(test_results: TestResults):
    print(test_results.test_name)

    if test_results.test_name == "a":
        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="db_connect"
        )  # database connection
        cursor = connection.cursor()
        empty = "test_results.test_name"
        print(type(empty))
        print(type(test_results.test_name))
        query = "INSERT INTO test_a (test_a_1,test_a_2,test_a_3,test_a_4,test_a_5,test_a_6,test_a_7,test_a_8,test_a_9,test_a_10,test_a_1_reaction_time,test_a_2_reaction_time,test_a_3_reaction_time,test_a_4_reaction_time,test_a_5_reaction_time,test_a_6_reaction_time,test_a_7_reaction_time,test_a_8_reaction_time,test_a_9_reaction_time,test_a_10_reaction_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        cursor.execute(
            query,
            (
                test_results.test_a_1,
                test_results.test_a_2,
                test_results.test_a_3,
                test_results.test_a_4,
                test_results.test_a_5,
                test_results.test_a_6,
                test_results.test_a_7,
                test_results.test_a_8,
                test_results.test_a_9,
                test_results.test_a_10,
                test_results.test_a_1_reaction_time,
                test_results.test_a_2_reaction_time,
                test_results.test_a_3_reaction_time,
                test_results.test_a_4_reaction_time,
                test_results.test_a_5_reaction_time,
                test_results.test_a_6_reaction_time,
                test_results.test_a_7_reaction_time,
                test_results.test_a_8_reaction_time,
                test_results.test_a_9_reaction_time,
                test_results.test_a_10_reaction_time,
            ),
        )

        connection.commit()  # commiting the connection
        connection.close()  # close the connection

    if test_results.test_name == "b":
        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="db_connect"
        )  # database connection
        cursor = connection.cursor()
        empty = "test_results.test_name"
        print(type(empty))
        print(type(test_results.test_name))
        query = "INSERT INTO test_b (test_b_1,test_b_2,test_b_3,test_b_4,test_b_5,test_b_6,test_b_7,test_b_8,test_b_9,test_b_10,test_b_1_reaction_time,test_b_2_reaction_time,test_b_3_reaction_time,test_b_4_reaction_time,test_b_5_reaction_time,test_b_6_reaction_time,test_b_7_reaction_time,test_b_8_reaction_time,test_b_9_reaction_time,test_b_10_reaction_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        cursor.execute(
            query,
            (
                test_results.test_b_1,
                test_results.test_b_2,
                test_results.test_b_3,
                test_results.test_b_4,
                test_results.test_b_5,
                test_results.test_b_6,
                test_results.test_b_7,
                test_results.test_b_8,
                test_results.test_b_9,
                test_results.test_b_10,
                test_results.test_b_1_reaction_time,
                test_results.test_b_2_reaction_time,
                test_results.test_b_3_reaction_time,
                test_results.test_b_4_reaction_time,
                test_results.test_b_5_reaction_time,
                test_results.test_b_6_reaction_time,
                test_results.test_b_7_reaction_time,
                test_results.test_b_8_reaction_time,
                test_results.test_b_9_reaction_time,
                test_results.test_b_10_reaction_time,
            ),
        )

        connection.commit()  # commiting the connection
        connection.close()  # close the connection


@app.post("/post_quest_res/")
async def post_quest_res(quest_res: Questionnaire):
    print(quest_res)
    if quest_res.test_name == "questionnaire_a":

        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="db_connect"
        )  # database connection
        cursor = connection.cursor()
        print(quest_res.test_name)
        print("adsasd")
        query = "INSERT INTO questionnaire_answers_a (gender,age_range,familiarity_tech,myRange1,myRange2,myRange3,myRange4,myRange5,myRange6,myRange7,myRange8,myRange9,myRange10,text_box) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        cursor.execute(
            query,
            (
                quest_res.gender,
                quest_res.age_range,
                quest_res.familiarity_tech,
                quest_res.myRange1,
                quest_res.myRange2,
                quest_res.myRange3,
                quest_res.myRange4,
                quest_res.myRange5,
                quest_res.myRange6,
                quest_res.myRange7,
                quest_res.myRange8,
                quest_res.myRange9,
                quest_res.myRange10,
                quest_res.text_box,
            ),
        )

        connection.commit()  # commiting the connection
        connection.close()  # close the connection
    elif quest_res.test_name == "questionnaire_b":

        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="db_connect"
        )  # database connection
        cursor = connection.cursor()
        print(quest_res.test_name)
        print("adsasd")
        query = "INSERT INTO questionnaire_answers_b (gender,age_range,familiarity_tech,myRange1,myRange2,myRange3,myRange4,myRange5,myRange6,myRange7,myRange8,myRange9,myRange10,text_box) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        cursor.execute(
            query,
            (
                quest_res.gender,
                quest_res.age_range,
                quest_res.familiarity_tech,
                quest_res.myRange1,
                quest_res.myRange2,
                quest_res.myRange3,
                quest_res.myRange4,
                quest_res.myRange5,
                quest_res.myRange6,
                quest_res.myRange7,
                quest_res.myRange8,
                quest_res.myRange9,
                quest_res.myRange10,
                quest_res.text_box,
            ),
        )

        connection.commit()  # commiting the connection
        connection.close()  # close the connection)


@app.get("/")
async def root():
    return {"message": "Pedestrian project backend :)"}


if __name__ == "__main__":
    uvicorn.run("main:app")
