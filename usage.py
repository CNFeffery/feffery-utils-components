import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyCompareSlider(
            firstItem=html.Div(
                style={
                    # 'width': 800,
                    'height': 500,
                    'background': 'yellow'
                }
            ),
            secondItem=html.Div(
                style={
                    # 'width': 800,
                    'height': 500,
                    'background': 'green'
                }
            ),
            boundsPadding=50,
            style={
                # 'width': 800,
                'height': 500
            },
            buttonStyle={
                'width': 32,
                'height': 32,
                'fontSize': 14
            },
            position=30
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
