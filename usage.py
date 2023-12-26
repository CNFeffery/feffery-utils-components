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
            littlePlanet=True
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)