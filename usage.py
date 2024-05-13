import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyBurger(
            type=t,
            color='white',
            size=18,
            distance='sm',
            toggled=True,
        )
        for t in [
            'default',
            'squash',
            'cross',
            'twirl',
            'fade',
            'slant',
            'spiral',
            'divide',
            'turn',
            'pivot',
            'sling',
            'squeeze',
            'spin',
            'rotate',
        ]
    ],
    style={
        'height': '100vh',
        'background': '#1a202c',
        'padding': '0 100px',
    },
)

if __name__ == '__main__':
    app.run(debug=True)
