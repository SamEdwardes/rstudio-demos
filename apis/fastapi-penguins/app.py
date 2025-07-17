import datetime as dt

import polars as pl
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Penguin(BaseModel):
    species: str | None = None
    island: str | None = None
    bill_length_mm: float | None = None
    bill_depth_mm: float | None = None
    flipper_length_mm: float | None = None
    body_mass_g: float | None = None
    sex: str | None = None
    year: int | None = None


class PenguinRaw(BaseModel):
    study_name: str = Field(alias="studyName")
    sample_number: int = Field(alias="Sample Number")
    species: str = Field(alias="Species")
    region: str = Field(alias="Region")
    island: str = Field(alias="Island")
    stage: str = Field(alias="Stage")
    individual_id: str = Field(alias="Individual ID")
    clutch_completion: str = Field(alias="Clutch Completion")
    date_egg: dt.date | None = Field(default=None, alias="Date Egg")
    culmen_length_mm: float | None = Field(default=None, alias="Culmen Length (mm)")
    culmen_depth_mm: float | None = Field(default=None, alias="Culmen Depth (mm)")
    flipper_length_mm: float | None = Field(default=None, alias="Flipper Length (mm)")
    body_mass_g: float | None = Field(default=None, alias="Body Mass (g)")
    sex: str = Field(alias="Sex")
    delta_15_n_o_oo: float | None = Field(default=None, alias="Delta 15 N (o/oo)")
    delta_13_c_o_oo: float | None = Field(default=None, alias="Delta 13 C (o/oo)")


# @app.get("/", response_class=RedirectResponse)
# def index():
#     return RedirectResponse("/docs")


@app.get("/penguins", response_model=list[Penguin])
def penguins(sample_size: int | None = None):
    url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
    penguins_df = pl.read_csv(url)
    if sample_size:
        penguins_df = penguins_df.sample(sample_size)
    penguins_response = [Penguin(**i) for i in penguins_df.to_dicts()]
    return penguins_response


@app.get("/raw_penguins", response_model=list[PenguinRaw])
def raw_penguins(sample_size: int | None = None):
    url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
    penguins_raw_df = pl.read_csv(url)
    if sample_size:
        penguins_raw_df = penguins_raw_df.sample(sample_size)
    penguins_raw_response = [PenguinRaw(**i) for i in penguins_raw_df.to_dicts()]
    return penguins_raw_response
