import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '开启色彩拾取',
            id='enable-eye-dropper'
        ),
        fuc.FefferyDiv(
            fuc.FefferyEyeDropper(
                id='eye-dropper'
            )
        ),

        html.Div(
            className='demo-div'
        ),

        fuc.FefferyStyle(
            rawStyle='''
.demo-div {
    width: 200px;
    height: 200px;
    background: green;
    border: 5px dashed red;
}
'''
        )
    ]
)


app.clientside_callback(
    '''(n_clicks) => true''',
    Output('eye-dropper', 'enable'),
    Input('enable-eye-dropper', 'n_clicks'),
    prevent_initial_call=True
)


if __name__ == '__main__':
    app.run(debug=True)
