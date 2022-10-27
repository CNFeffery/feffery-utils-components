import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            shadow='hover-shadow',
            style={
                'width': '400px',
                'height': '200px',
                'marginBottom': '20px'
                # 'border': '1px solid grey'
            }
        ),

        fuc.FefferyDiv(
            shadow='always-shadow',
            style={
                'width': '400px',
                'height': '200px',
                # 'border': '1px solid grey'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
