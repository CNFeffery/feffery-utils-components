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
        fuc.FefferyJsonViewer(
            data={
                'int示例': 999,
                'float示例': 0.999,
                'string示例': '我爱dash',
                '数组示例': [0, 1, 2, 3],
                '字典示例': {'a': 1, 'b': 2, 'c': 3},
            }
        ),
        fuc.FefferyJsonViewer(
            data={
                'int示例': 999,
                'float示例': 0.999,
                'string示例': '我爱dash',
                '数组示例': [0, 1, 2, 3],
                '字典示例': {'a': 1, 'b': 2, 'c': 3},
            },
            editable=True,
            addible=True,
            deletable=True,
        ),
    ],
    style=style(padding=100),
)


if __name__ == '__main__':
    app.run(debug=True)
