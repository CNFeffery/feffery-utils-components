import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '手动刷新',
            id='manual-refresh'
        ),
        fuc.FefferySliderCaptcha(
            id='demo-slider-captcha',
            imgSrc='/assets/demo.jpg',
            imgWidth=360
        ),
        html.Pre(id='demo-output')
    ],
    style={
        'padding': '300px 100px'
    }
)


@app.callback(
    Output('demo-slider-captcha', 'refresh'),
    Input('manual-refresh', 'n_clicks'),
    prevent_initial_call=True
)
def manual_refresh(n_clicks):
    return True


@app.callback(
    Output('demo-output', 'children'),
    Input('demo-slider-captcha', 'verifyResult')
)
def update_output(verifyResult):
    return json.dumps(
        verifyResult,
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
