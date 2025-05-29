if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            id='event-listen-target',
            style=style(height=400, background='lightblue'),
        ),
        fuc.FefferyEventListener(
            id='event-listener',
            eventName=[
                'click',
                'dblclick',
                'contextmenu',
                'mouseenter',
                'mouseleave',
            ],
            targetSelector='#event-listen-target',
            handler='(e) => dash_clientside.set_props("event-listen-target", {children: e.type})',
        ),
    ],
    style=style(padding=50),
)


if __name__ == '__main__':
    app.run(debug=True)
