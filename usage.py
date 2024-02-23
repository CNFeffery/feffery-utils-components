import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Img(
            src='assets/报告背景示例.png',
            style={
                'width': '100%',
                'height': '100%',
                'objectFit': 'contain',
                'display': 'block'
            }
        ),
        fuc.FefferyFixed(
            '测试',
            mode='follow-image',
            followImageWidth=1920,
            followImageHeight=1079,
            followImageContainerPosition=[0, 0],
            followImageContainerSize=[0.5, 0.5],
            style={
                'background': '#1890ff',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )
    ],
    style={
        'height': '100vh'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
