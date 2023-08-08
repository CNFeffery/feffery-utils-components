import dash
import json
from dash import html, dcc
import feffery_utils_components.alias as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            'press me',
            id='long-press-target',
        ),
        fuc.LongPress(
            id='long-press-demo',
            targetId='long-press-target',
            # delay=3000
        ),
        html.Pre(id='long-press-output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('long-press-output', 'children'),
    Input('long-press-demo', 'pressCounts')
)
def demo(pressCounts):

    return str(dict(pressCounts=pressCounts))


if __name__ == '__main__':
    app.run(debug=True)
