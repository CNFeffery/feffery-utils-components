
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [

        fuc.FefferyStyle(
            rawStyle='''
.style-demo {
    background: white;
    width: 400px;
    height: 200px;
    border: 1px solid #f0f0f0;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
}

.style-demo:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 12px rgba(0, 0, 0, .12);
    transition: 0.3s;
}
'''
        ),

        html.Div(
            '鼠标移入查看效果',
            className='style-demo'
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
