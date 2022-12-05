from pydantic import BaseModel


class testMod(BaseModel):
    title: str
    answer_type: int
    answer_choo: list
    answer_true: list
    num: int


class infoMod(BaseModel):
    numbers: int
    statime: str
    endtime: str
    settime: str
    name: str
    grp_numbers: int
    mgroup: int
    sources: int
