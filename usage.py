import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            style={
                'height': 50,
                'border': '1px solid black',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'marginBottom': 8,
            },
        )
        for i in range(100)
    ],
    style={'padding': 50},
)


if __name__ == '__main__':
    app.run(debug=True)
