if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html
    import feffery_antd_components as fac
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    fuc.FefferyDiv(

        fac.AntdTree(
            id='tree-demo',
            treeData=[
                {
                    'title': f'数仓{i}',
                    'key': f'数仓{i}',
                    'icon': 'antd-database',
                    'children': [
                        {
                            'title': f'业务表{i}-{j}',
                            'key': f'业务表{i}-{j}',
                            'icon': 'antd-table'
                        }
                        for j in range(10)
                    ]
                }
                for i in range(1000)
            ],
            defaultExpandAll=True,
            height=25
        ),
        id='listen-height',
        style={
            'background': 'white',
            'borderRadius': '8px',
            'padding': '25px',
            'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
            'height': '100%'
        }
    ),
    style={
        'padding': '20px',
        'height': '100vh'
    }
)


@app.callback(
    Output('tree-demo', 'height'),
    Input('listen-height', '_height')
)
def update_tree_height(_height):

    print(_height)

    if _height:
        return _height - 50

    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
