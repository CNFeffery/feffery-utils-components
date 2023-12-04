import dash
import uuid
import random
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True, compress=True)

app.layout = html.Div(
    [

        html.Div(
            [
                fuc.FefferyFancyButton(
                    '加载子元素',
                    id='auto-animate-demo-load-children'
                ),
                fuc.FefferyFancyButton(
                    '追加子元素',
                    id='auto-animate-demo-push-child'
                ),
                fuc.FefferyFancyButton(
                    '随机打乱顺序',
                    id='auto-animate-demo-random-order'
                ),
                fuc.FefferyFancyButton(
                    '随机删除一项',
                    id='auto-animate-demo-random-delete'
                )
            ]
        ),

        fuc.FefferyAutoAnimate(
            id='auto-animate-demo-container'
        )
    ],
    style={
        'padding': 10,
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        'flex-direction': 'column'
    }
)


@app.callback(
    Output('auto-animate-demo-container', 'children'),
    [Input('auto-animate-demo-load-children', 'nClicks'),
     Input('auto-animate-demo-push-child', 'nClicks'),
     Input('auto-animate-demo-random-order', 'nClicks')],
    Input('auto-animate-demo-random-delete', 'nClicks'),
    State('auto-animate-demo-container', 'children'),
    prevent_initial_call=True
)
def auto_animate_demo(load_children,
                      push_chjild,
                      random_order,
                      random_delete,
                      old_children):

    if dash.ctx.triggered_id == 'auto-animate-demo-load-children':
        new_children = []
        for i in range(3):
            current_uuid = str(uuid.uuid4())
            new_children.append(
                fuc.FefferyDiv(
                    current_uuid,
                    id=current_uuid,
                    style={
                        'width': '460px',
                        'height': '40px',
                        'marginTop': '5px',
                        'border': '1px solid #e1dfdd',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'cursor': 'pointer'
                    },
                    shadow='hover-shadow'
                )
            )
        return new_children

    elif dash.ctx.triggered_id == 'auto-animate-demo-push-child':
        current_uuid = str(uuid.uuid4())
        return [
            *old_children,
            fuc.FefferyDiv(
                current_uuid,
                id=current_uuid,
                style={
                    'width': '460px',
                    'height': '40px',
                    'marginTop': '5px',
                    'border': '1px solid #e1dfdd',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'cursor': 'pointer'
                },
                shadow='hover-shadow'
            )
        ]

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-order':
        random.shuffle(old_children)
        return old_children

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-delete':
        delete_idx = random.randint(0, len(old_children)-1)

        return [
            child for i, child in enumerate(old_children)
            if i != delete_idx
        ]


if __name__ == '__main__':
    app.run(debug=True)
