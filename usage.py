import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyWheelColorPicker(
            id='wheel-color-picker-demo'
        ),

        html.Div(
            id='wheel-color-picker-demo-output',
            style={
                'width': '200px',
                'height': '200px',
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'center',
                'borderRadius': '5px',
                'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                'transition': '0.25s'
            }
        )
    ],
    style={
        'padding': '50px'
    }
)


@app.callback(
    [Output('wheel-color-picker-demo-output', 'style'),
     Output('wheel-color-picker-demo-output', 'children')],
    Input('wheel-color-picker-demo', 'color'),
    State('wheel-color-picker-demo-output', 'style')
)
def wheel_color_picker_demo(color, old_style):

    return [
        {
            **old_style,
            'background': color
        },
        color
    ]


if __name__ == '__main__':
    app.run(debug=True)
