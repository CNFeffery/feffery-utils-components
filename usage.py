import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyPageLeave(id='page-leave-demo'),
        html.Div(id='output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('output', 'children'),
    Input('page-leave-demo', 'isLeft'),
    prevent_initial_call=True
)
def demo(isLeft):

    return f'isLeft: {isLeft}'


if __name__ == '__main__':
    app.run(debug=True)
