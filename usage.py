import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyPhotoSphereViewer(
            src='https://uploads.codesandbox.io/uploads/user/01c56c10-96fe-4c29-835d-116aac7b5710/MVb7-Test_Pano.jpg',
            width='100%',
            height='100vh',
            littlePlanet=True,
            **dict(
                caption='导航栏标题测试',
                navbar=[
                    'zoom',
                    'move',
                    'download',
                    'caption',
                    'fullscreen'
                ],
                # lang={
                #     'zoomOut': '缩小',
                #     'zoomIn': '放大',
                #     'moveUp': '上移',
                #     'moveDown': '下移',
                #     'moveLeft': '左移',
                #     'moveRight': '右移',
                #     'download': '下载',
                #     'fullscreen': '全屏',
                #     'loadError': '资源加载失败',
                #     'littlePlanet': '小星球模式'
                # },
                # loadingImg='data:image/png;base64,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',
                loadingTxt='资源加载中',
                mousewheel=True,
                mousemove=True,
                moveSpeed=10,
                zoomSpeed=10
            )
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
