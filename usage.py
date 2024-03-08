import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferySortable(
            id='input',
            items=[
                {
                    'key': f'子项{i}',
                    'content': [
                        f'子项{i}',
                        dcc.Checklist(
                            id=f'checklist{i}',
                            options=[f'选项{i}' for i in range(1, 3)]
                        )
                    ],
                    'style': {
                        'borderBottom': '1px solid lightgrey',
                        'background': 'white',
                        'padding': '5px',
                        'height': 50 + i * 20,
                        'border': '1px solid #bfbfbf'
                    },
                    'draggingStyle': {
                        'boxShadow': '0px 0px 12px rgba(0, 0, 0, 0.12)',
                        'borderBottom': '1px solid transparent'
                    }
                }
                for i in range(1, 6)
            ],
            currentOrder=['子项2', '子项3', '子项1', '子项4', '子项5'],
            itemDraggingScale=1.025,
            handleStyle={
                'color': '#adb5bd'
            },
            handleClassName={
                '&:hover': {
                    'background': '#f1f3f5'
                },
                'padding': '4px',
                'borderRadius': '8px'
            },
            style={
                'width': 400
            }
        ),

        html.Pre(id='output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('output', 'children'),
    Input('input', 'currentOrder')
)
def sortable_list_demo(currentOrder):

    return str(currentOrder)


@app.callback(
    Output('checklist2', 'id'),
    Input('checklist2', 'value')
)
def demo(value):

    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
