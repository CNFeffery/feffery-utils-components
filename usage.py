import dash
import json
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        '网页测试',
        fuc.FefferyDebugGuardian(
            strategy='debugger-then-auto-close',
            # jsString='console.log("禁止调试")'
            # jsString='document.write('')'
        )
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
