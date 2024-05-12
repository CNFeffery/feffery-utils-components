import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyPhotoSphereViewer(
            src='https://photo-sphere-viewer-data.netlify.app/assets/sphere.jpg',
            littlePlanet=True,
            height='100%',
            width='100%',
            loadingTxt='载入中',
            navbar=['autorotate'],
            lang={'autorotate': '自动旋转'},
            plugins=[
                {
                    'type': 'Autorotate',
                    'autorotateSpeed': '10rpm',
                }
            ],
        )
    ],
    style={'height': '100vh'},
)

if __name__ == '__main__':
    app.run(debug=True)
