import altair as alt
import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
    data = pd.read_csv(url)
    return data


raw_data = load_data()

with st.sidebar:
    selected_island = st.selectbox(
        "Island", options=["All"] + list(raw_data["island"].unique())
    )
    selected_species = st.selectbox(
        "Species", options=["All"] + list(raw_data["species"].unique())
    )

st.write("# Meeting the penguins!")

col_text, col_image = st.columns([8, 4])

with col_text:
    st.write("""
    Data were collected and made available by Dr. Kristen Gorman and the Palmer
    Station, Antarctica LTER, a member of the Long Term Ecological Research Network.
    """)

with col_image:
    st.image(
        "https://allisonhorst.github.io/palmerpenguins/reference/figures/lter_penguins.png",
        width=150,
    )


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    if selected_island != "All":
        df = df.loc[df["island"] == selected_island]
    if selected_species != "All":
        df = df.loc[df["species"] == selected_species]
    return df


filtered_data = apply_filters(raw_data)


scatter_plot = (
    alt.Chart(filtered_data)
    .mark_circle(size=60)
    .encode(
        alt.X("flipper_length_mm:Q"),
        alt.Y("bill_length_mm:Q"),
        alt.Color("species:N", legend=None),
        tooltip=["flipper_length_mm", "bill_length_mm", "species"],
    )
    .interactive()
)

histogram = (
    alt.Chart(filtered_data)
    .mark_bar()
    .encode(
        alt.X("flipper_length_mm:Q"),
        alt.Y("count()", stack=None),
        alt.Color("species:N"),
    )
    .interactive()
)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.write("#### Bill Length vs. Flipper Length")
    st.altair_chart(scatter_plot)

with chart_col2:
    st.write("#### Distribution of Flipper Length")
    st.altair_chart(histogram)
