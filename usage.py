import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            fuc.FefferyMotion(
                '示例',
                id='motion-demo',
                style={
                    'border': '1px dashed #71afe5',
                    'width': '100px',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                },
                animate={
                    'transform': 'translateX(300px) rotate(180deg)',
                    'borderRadius': '100%',
                },
                transition={
                    'duration': 2,
                },
                destroyWhenAnimated=True,
            ),
            html.Pre(id='animated'),
        ],
        style={'padding': 50},
    )
)


@app.callback(
    Output('animated', 'children'),
    Input('motion-demo', 'animated'),
    prevent_initial_call=True,
)
def demo(animated):
    return f'animated: {animated}'


if __name__ == '__main__':
    app.run(debug=True)
