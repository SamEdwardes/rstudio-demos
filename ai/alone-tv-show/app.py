"""Shiny for Python app to explore the Alone TV show contestant data Thursday August 27, 2026 07:53."""

from pathlib import Path

import polars as pl
from plotnine import aes, geom_histogram, ggplot, labs, theme_minimal
from shiny import App, reactive, render, ui

COLOR_CHOICES = {
    "None": None,
    "Season": "Season",
    "Gender": "Gender",
    "Status": "Status",
}

CSV_PATH = Path(__file__).parent / "data" / "alone-contestants.csv"
CONTESTANTS = pl.read_csv(CSV_PATH)

SEASONS = sorted(CONTESTANTS.get_column("Season").unique().to_list())
GENDERS = sorted(CONTESTANTS.get_column("Gender").unique().to_list())
STATUSES = sorted(CONTESTANTS.get_column("Status").unique().to_list())
AGE_MIN, AGE_MAX = (
    CONTESTANTS.get_column("Age").min(),
    CONTESTANTS.get_column("Age").max(),
)
DAYS_MIN, DAYS_MAX = (
    CONTESTANTS.get_column("Days Lasted").min(),
    CONTESTANTS.get_column("Days Lasted").max(),
)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            "color_by", "Histogram colour", choices=list(COLOR_CHOICES.keys()), selected="None"
        ),
        ui.input_selectize(
            "season",
            "Season",
            choices=[str(s) for s in SEASONS],
            selected=[str(s) for s in SEASONS],
            multiple=True,
        ),
        ui.input_checkbox_group(
            "gender", "Gender", choices=GENDERS, selected=GENDERS
        ),
        ui.input_checkbox_group(
            "status", "Status", choices=STATUSES, selected=STATUSES
        ),
        ui.input_slider(
            "age", "Age", min=AGE_MIN, max=AGE_MAX, value=[AGE_MIN, AGE_MAX]
        ),
        ui.input_slider(
            "days", "Days Lasted", min=DAYS_MIN, max=DAYS_MAX, value=[DAYS_MIN, DAYS_MAX]
        ),
        title="Filters",
    ),
    ui.head_content(
        ui.tags.style("body { background-color: #F9F9F7; }")
    ),
    ui.card(
        ui.card_header("Days Lasted Distribution"),
        ui.output_plot("days_histogram"),
    ),
    ui.card(
        ui.card_header("Contestants"),
        ui.output_data_frame("contestants_table"),
    ),
    title="🐻 Alone TV Show Explorer",
    fillable=True,
)


def server(input, output, session):
    @reactive.calc
    def filtered_data() -> pl.DataFrame:
        seasons_selected = [int(s) for s in input.season()]
        return CONTESTANTS.filter(
            pl.col("Season").is_in(seasons_selected),
            pl.col("Gender").is_in(input.gender()),
            pl.col("Status").is_in(input.status()),
            pl.col("Age").is_between(input.age()[0], input.age()[1]),
            pl.col("Days Lasted").is_between(input.days()[0], input.days()[1]),
        )

    @render.plot
    def days_histogram():
        color_column = COLOR_CHOICES[input.color_by()]
        data = filtered_data()

        if color_column is None:
            mapping = aes(x="Days Lasted")
            geom = geom_histogram(binwidth=10, boundary=0, fill="#2c3e50", color="white")
        else:
            # Cast to string so numeric columns like Season are treated as
            # discrete groups rather than a continuous color gradient.
            data = data.with_columns(pl.col(color_column).cast(pl.String))
            mapping = aes(x="Days Lasted", fill=color_column)
            geom = geom_histogram(binwidth=5, boundary=0, color="white")

        return (
            ggplot(data, mapping)
            + geom
            + labs(x="Days Lasted", y="Number of Contestants", fill=input.color_by())
            + theme_minimal()
        )

    @render.data_frame
    def contestants_table():
        return render.DataGrid(filtered_data(), filters=False)


app = App(app_ui, server)
