import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
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
            # draggable=False
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
