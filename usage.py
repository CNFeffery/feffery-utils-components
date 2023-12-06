
import feffery_utils_components as fuc
import dash
from dash.dependencies import Input, Output, State
from dash import html
import random

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [

        html.Div(
            [
                html.Span('提示：按下快捷组合键'),
                html.Span('ctrl+s'),
                html.Span('唤出本示例中的快捷指令面板，在搜索框中输入内容进行远程选项搜索')
            ]
        ),
        fuc.FefferyShortcutPanel(
            id='shortcut-panel-demo',
            openHotkey='cmd+s,ctrl+s',
            data=[]
        )
    ]
)


@app.callback(
    Output('shortcut-panel-demo', 'data'),
    Input('shortcut-panel-demo', 'searchValue'),
    prevent_initial_call=True
)
def shortcut_panel_demo(searchValue):

    return [
        {
            'id': f'{searchValue}搜索结果{i}',
            'title': f'{searchValue}搜索结果{i}',
        }
        for i in range(1, random.randint(3, 6))
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
