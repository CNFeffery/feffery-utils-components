import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(),

        html.Div(
            className='demo-div'
        ),

        fuc.FefferyStyle(
            rawStyle='''
.demo-div {
    width: 200px;
    height: 200px;
    background: green;
    border: 5px dashed red;
}
'''
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)
