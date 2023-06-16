import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferySortableList(
            id='input',
            items=[
                {
                    'key': f'子项{i}',
                    'content': html.Div(
                        f'子项{i}',
                        style={
                            'padding': '10px 6px'
                        }
                    ),
                    'style': {
                        'borderBottom': '1px solid lightgrey',
                        'background': 'white',
                        'padding': '0 5px'
                    },
                    'draggingStyle': {
                        'boxShadow': '0px 0px 12px rgba(0, 0, 0, 0.12)',
                        'borderBottom': '1px solid transparent'
                    }
                }
                for i in range(1, 6)
            ],
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
                'width': 300
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


if __name__ == '__main__':
    app.run(debug=True)
