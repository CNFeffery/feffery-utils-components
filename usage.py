import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyCountUp(
            end=666.66,
            decimals=2,
            duration=1,
            className='gradient-text',
            style={
                'fontSize': 28,
                'fontFamily': 'SimHei',
                'color': 'green',
            },
        )
    ],
    style={'padding': 50},
)


if __name__ == '__main__':
    app.run(debug=True)
