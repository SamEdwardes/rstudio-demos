from fasthtml.common import *

app = FastHTML()

count = 0

nav = Div(
    A("Home", href="/"),
    A("Page 2", href="/page2"),
)

@app.get("/")
def home():
    return Title("Count Demo"), Main(
        nav,
        H1("Count Demo"),
        P(f"Count is set to {count}", id="count"),
        Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML")
    )

@app.get("/page2")
def page2():
    return Title("Count Demo"), Main(
        nav,
        H1("Page 2"),
        P(f"Count is set to {count}", id="count"),
        Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML")
    )

@app.post("/increment")
def increment():
    print("incrementing")
    global count
    count += 1
    return f"Count is set to {count}"


serve()