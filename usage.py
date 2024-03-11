import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyAnimatedImage(
            src="https://shoelace.style/assets/images/walk.gif",
            alt="Animation of untied shoes walking on pavement",
            play=True,
            style={
                'width': 300
            }
        ),
        fuc.FefferyAnimatedImage(
            src="https://shoelace.style/assets/images/tie.webp",
            alt="Animation of a shoe being tied",
            play=True,
            style={
                'width': 300
            }
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
