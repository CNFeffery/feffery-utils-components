if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    from dash.dependencies import Input
    import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    fuc.FefferyListenUnload(
        id='unload-demo', confirmBeforeUnload=True
    ),
)


@app.callback(Input('unload-demo', 'unloaded'))
def show_unloaded(unloaded):
    print(f'unloaded: {unloaded}')


if __name__ == '__main__':
    app.run(debug=True)
