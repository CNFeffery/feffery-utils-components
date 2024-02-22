import json
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        # # 背景图
        # html.Img(
        #     src=dash.get_asset_url('bg.png'),
        #     style={
        #         'width': '100%',
        #         'height': '100%',
        #         'objectFit': 'contain',
        #         'display': 'block'
        #     }
        # ),
        # 示例边界范围
        html.Div(
            fuc.FefferyDraggable(
                fuc.FefferyResizable(
                    html.Div(
                        id='show-bounding',
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'border': '2px solid #1890ff',
                            'boxSizing': 'border-box',
                            'padding': 2
                        }
                    ),
                    id='demo-resizable',
                    boundsSelector='#demo-bounds',
                    defaultSize={
                        'width': 500,
                        'height': 120
                    }
                ),
                id='demo-draggable',
                initialX=0,
                initialY=0,
                showDragLine=True,
                boundsSelector='#demo-bounds',
                # draggable=False,
            ),
            id='demo-bounds',
            style={
                'position': 'relative',
                'backgroundColor': '#f0f0f0',
                'height': 'calc(100vh - 100px)',
                'margin': '0 auto'
            }
        )
    ],
    style={
        'padding': '50px 100px 0 100px',
        'position': 'relative'
    }
)


@app.callback(
    Output('show-bounding', 'children'),
    [Input('demo-draggable', 'x'),
     Input('demo-draggable', 'y'),
     Input('demo-resizable', 'size'),
     Input('demo-draggable', 'isFocusWithin')]
)
def show_bounding(x, y, size, isFocusWithin):

    if size:
        return f'x: {x}, y: {y}, width: {size["width"]}, height: {size["height"]}, isFocusWithin: {isFocusWithin}'


if __name__ == '__main__':
    app.run_server(debug=True)
