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
        fuc.FefferySliderCaptcha(
            id='slider-captcha',
            mode='slider',
            tipText={
                'default': '请按住滑块，拖动到最右边',
                'moving': '请按住滑块，拖动到最右边',
                'error': '验证失败，请重新操作',
                'success': '验证成功',
            },
            block=True,
            style=style(width='100%'),
        ),
    ],
    style=style(padding=50),
)


if __name__ == '__main__':
    app.run(debug=True)
