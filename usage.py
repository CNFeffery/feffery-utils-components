import dash
import json
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyEmojiPicker(
            id='feffery-emoji-picker',
            locale='zh'
        ),
        html.Pre(id='output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('output', 'children'),
    [Input('feffery-emoji-picker', 'value'),
    Input('feffery-emoji-picker', 'clickOutsideNums')],
    prevent_initial_call=True
)
def display_output(value, clickOutsideNums):
    data = {
        '选择的emoji信息': value,
        '点击选择器之外区域的次数': clickOutsideNums
    }
    return json.dumps(data, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    app.run(debug=True)
