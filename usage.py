import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Div(
            fuc.FefferyImageGallery(
                images=[
                    {
                        'original': "https://picsum.photos/id/1018/1000/600/",
                        'thumbnail': "https://picsum.photos/id/1018/250/150/",
                    },
                    {
                        'original': "https://picsum.photos/id/1015/1000/600/",
                        'thumbnail': "https://picsum.photos/id/1015/250/150/",
                    },
                    {
                        'original': "https://picsum.photos/id/1019/1000/600/",
                        'thumbnail': "https://picsum.photos/id/1019/250/150/",
                    }
                ]
            ),
            style={
                'width': 800,
                'height': 600
            }
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
