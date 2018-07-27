from pfont import *

lipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi
convallis eu odio quis euismod. Quisque aliquet dui congue maximus
gravida. Nullam justo est, semper quis laoreet sed, facilisis vel est.
Pellentesque accumsan lectus ullamcorper eros vulputate auctor. Proin
dapibus cursus turpis, vehicula fermentum tellus luctus in. Morbi
tincidunt, urna nec varius convallis, massa orci suscipit lectus,
suscipit tristique felis nibh id magna. Praesent lobortis tincidunt
tortor. Aliquam non sem vel ipsum ultricies venenatis. """

unica_one = create_font('fonts/UnicaOne.ttf', 72)
open_sans = create_font('fonts/OpenSans-Bold.ttf', 12)

with render_font():
    text_font(unica_one)
    text("Hello\nWorld", (50, 50))

    text_font(open_sans)
    text(lipsum, (270, 44), wrap_at=60)

