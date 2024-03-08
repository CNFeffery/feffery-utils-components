import dash
import json
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, ALL

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferySortable(
            id='sortable-demo',
            value='子项1',
            maxTranslateX=0,
            # multiple=True,
            allowNoValue=False,
            selectedStyle={
                'border': '1px solid red'
            },
            items=[
                {
                    'key': f'子项{i}',
                    'content': [
                        f'子项{i}',
                        dcc.Checklist(
                            id={
                                'type': 'checklist-demo',
                                'index': f'子项{i}'
                            },
                            options=[f'选项{j}' for j in range(1, 3)]
                        )
                    ],
                    'style': {
                        'border': '1px solid lightgrey',
                        'background': 'white',
                        'padding': '5px',
                        'marginBottom': 3
                    },
                    'draggingStyle': {
                        'boxShadow': '0px 0px 12px rgba(0, 0, 0, 0.12)',
                        'border': '1px solid transparent'
                    }
                }
                for i in range(1, 11)
            ],
            itemDraggingScale=1.05,
            style={
                'width': 400,
                'padding': '4px 20px',
                'background': '#bfbfbf',
                'maxHeight': 600,
                'overflowY': 'auto'
            }
        ),
        html.Pre(
            id='output-demo'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('output-demo', 'children'),
    [
        Input('sortable-demo', 'currentOrder'),
        Input(
            {
                'type': 'checklist-demo',
                'index': ALL
            },
            'value'
        )
    ]
)
def update_params(currentOrder, values):

    return json.dumps(
        {
            'currentOrder': currentOrder,
            'values': {
                item['id']['index']: item.get('value')
                for item in dash.ctx.inputs_list[1]
            }
        },
        ensure_ascii=False,
        indent=4
    )


if __name__ == '__main__':
    app.run(debug=True)
