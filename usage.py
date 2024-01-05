import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyDPlayer()
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
