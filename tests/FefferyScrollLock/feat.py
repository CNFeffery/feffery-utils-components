if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_antd_components as fac
    import feffery_utils_components as fuc
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyScrollLock(id='scroll-lock'),
        fuc.FefferyScrollLock(
            id='scroll-lock-target',
            target='demo-target',
        ),
        fac.AntdButton(
            '锁定/取消锁定整体页面',
            id='toggle-scroll-lock',
            type='primary',
        ),
        fac.AntdButton(
            '锁定/取消锁定目标',
            id='toggle-scroll-lock-target',
            type='primary',
        ),
        html.Div(
            '测试' * 100000,
            id='demo-target',
            style=style(
                maxHeight='120vh', overflow='scroll'
            ),
        ),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('scroll-lock', 'locked'),
    Input('toggle-scroll-lock', 'nClicks'),
    State('scroll-lock', 'locked'),
    prevent_initial_call=True,
)
def toggle_scroll_lock(nClicks, locked):
    return not locked


@app.callback(
    Output('scroll-lock-target', 'locked'),
    Input('toggle-scroll-lock-target', 'nClicks'),
    State('scroll-lock-target', 'locked'),
    prevent_initial_call=True,
)
def toggle_scroll_lock_target(nClicks, locked):
    return not locked


if __name__ == '__main__':
    app.run(debug=True)
