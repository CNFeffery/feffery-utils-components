import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [fuc.FefferyCountUp(end=99999, enableScrollSpy=True)],
    style={'padding': '2000px 50px'},
)

if __name__ == '__main__':
    app.run(debug=True)
