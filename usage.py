
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H5(_type),
                        fuc.FefferyExtraSpinner(
                            type=_type,
                            style={
                                'marginBottom': '25px'
                            }
                        )
                    ]
                )
                for _type in [
                    "ball", "swap", "bars", "grid", "wave", "push", "firework",
                    "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
                    "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
                    "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
                    "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
                ]
            ],
            style={
                'marginBottom': '100px'
            }
        ),
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
