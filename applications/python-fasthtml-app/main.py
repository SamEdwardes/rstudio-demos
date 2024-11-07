import random
from fasthtml import common as fh
from fasthtml import ft


app = fh.FastHTML()

@app.route("/")
def home():
  return fh.Html(
     fh.Head(fh.Title("Home")),
     fh.Body(
         fh.H1("Welcome to FastHTML"),
         fh.Div("This is a simple web framework for Python"),
         ft.Button(
            "Generate random number",
            hx_get="/random_number",
            hx_target="#random-number",
            hx_swap="innerHTML"
        ),
         ft.P(id="random-number")
     )
  )

@app.route("/random_number")
def random_number():
    return ft.P(random.randint(1, 100))


if __name__ == "__main__":
    fh.serve(reload=True)