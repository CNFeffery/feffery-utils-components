import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyMediaQuery(id='media-query-demo',
                              query='(min-width: 480px)'),
        html.Div(id='output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('output', 'children'),
    Input('media-query-demo', 'isMatch'),
    prevent_initial_call=True
)
def demo(isMatch):

    return f'isMatch: {isMatch}'


if __name__ == '__main__':
    app.run(debug=True)
