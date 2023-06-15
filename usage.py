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
                    'id': f'子项{i}',
                    'content': html.Div(
                        f'子项{i}',
                        style={
                            'padding': f'{10+i*5}px 6px'
                        }
                    ),
                    'style': {
                        'borderBottom': '1px solid lightgrey'
                    }
                }
                for i in range(1, 6)
            ],
            handleStyle={
                'color': '#919eab',
                # 'cursor': 'move'
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
def demo(_):

    return str(_)


if __name__ == '__main__':
    app.run(debug=True)
