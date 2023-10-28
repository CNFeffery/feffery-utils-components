import json
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyRawHTML(
            htmlString='''
<div style="width: 300px;height: 150px;box-shadow: 0px 0px 12px rgba(0, 0, 0, .12); display: flex;justify-content: center;align-items: center;">
    示例
</ div>
'''
        )

    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
