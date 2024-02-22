import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        # 背景图
        html.Img(
            src=dash.get_asset_url('bg.png'),
            style={
                'width': '100%',
                'height': '100%',
                'objectFit': 'contain'
            }
        ),

        fuc.FefferyDraggable(
            fuc.FefferyResizable(
                html.Div(
                    style={
                        'display': 'flex',
                        'height': '100%',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'border': '1px solid #1890ff',
                        'boxSizing': 'border-box',
                    }
                ),
                defaultSize={
                    'width': 200,
                    'height': 50
                }
            ),
            initialX=400,
            initialY=200,
            showDragLine=True,
            dragLineColors=['red', 'yellow'],
            # draggable=False
        )
    ],
    style={
        'height': '100vh',
        'position': 'relative'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
