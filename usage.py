import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyGrid(
            placeholder='请从上方区域拖拽对应的组件到下方区域',
            layouts=[],
            cols=1,
            rowHeight=100,
            placeholderBorderRadius='5px',
            margin=[25, 25],
            isResizable=False,
            style={'border': '1px dashed #e1dfdd'},
        )
    ],
    style={'padding': 50},
)

if __name__ == '__main__':
    app.run(debug=True)
