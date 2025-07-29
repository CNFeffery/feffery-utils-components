if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = fuc.FefferyTopProgress(
    html.Div(
        fuc.FefferyFancyButton('状态切换', id='input-demo'),
        style=style(padding=50),
    ),
    id='top-progress-demo',
    manual=True,
)


@app.callback(
    Output('top-progress-demo', 'spinning'),
    Input('input-demo', 'nClicks'),
    State('top-progress-demo', 'spinning'),
    prevent_initial_call=True,
)
def demo(nClicks, spinning):
    return not spinning


if __name__ == '__main__':
    app.run(debug=True)
