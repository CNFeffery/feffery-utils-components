import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyPhotoSphereViewer(
            src='https://photo-sphere-viewer-data.netlify.app/assets/sphere.jpg',
            width='100%',
            height='100vh',
            littlePlanet=True,
            navbar=['zoom', 'move', 'download', 'caption', 'fullscreen'],
            loadingTxt='载入中',
            lang={
                'littlePlanetButton': '小星球模式',
                'zoomOut': '缩小',
                'zoomIn': '放大',
                'moveLeft': '左移',
                'moveRight': '右移',
                'moveUp': '上移',
                'moveDown': '下移',
                'download': '下载',
                'fullscreen': '全屏'
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
