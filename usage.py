
import feffery_utils_components as fuc
import dash
from dash.dependencies import Input, Output, State
from dash import html
import random

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [


        fuc.FefferyGrid(
            [
                fuc.FefferyGridItem(
                    str(i),
                    key=str(i),
                    style={
                        'height': '100%',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                )
                for i in range(10)
            ],
            layouts=[
                dict(
                    i=str(i),
                    x=i,
                    y=i+1,
                    w=1,
                    h=i+i % 2+1
                )
                for i in range(5)
            ],
            cols=5,
            rowHeight=75,
            placeholderBorderRadius='5px',
            margin=[25, 25],
            style={
                'border': '1px dashed #e1dfdd'
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
