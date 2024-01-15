import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyNetBackground(
            html.Div(
                'Net 3D背景效果',
                style={
                    'color': 'white',
                    'fontSize': '55px',
                    'top': '45%',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                }
            ),
            id='net-background',
            minHeight=600,
            style={
                'height': '100vh'
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
