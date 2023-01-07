if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyShortcutPanel(
            data=[
                {
                    'id': f'指令{i}',
                    'title': f'指令{i}',
                    'handler': f'() => alert("指令{i}")'
                }
                for i in range(20)
            ],
            open=True
        )
    ],
    style={
        'height': '2000px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
