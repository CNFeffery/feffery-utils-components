import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyLocalLargeStorage(
            id='local-large-storage-test',
            data='9'*10000000,
            # initialSync=True
        ),

        html.Div(
            id='output-demo',
            style={
                'wordWrap': 'break-word'
            }
        )
    ],
    style={
        'padding': 50
    }
)


app.clientside_callback(
    '''(data) => JSON.stringify(data)''',
    Output('output-demo', 'children'),
    Input('local-large-storage-test', 'data')
)


if __name__ == '__main__':
    app.run(debug=True)
