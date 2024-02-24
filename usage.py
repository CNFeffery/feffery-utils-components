import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            style={
                'height': '50vw',
                'border': '1px solid red'
            }
        )
    ],
    style={
        'height': 10000,
        'paddingTop': 800,
        'paddingLeft': '10vw'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
