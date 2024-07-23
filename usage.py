import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyGrid(
            [
                fuc.FefferyGridItem(
                    '测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试',
                    key=str(i),
                    style={
                        # 'height': '100%',
                        # 'display': 'flex',
                        # 'justifyContent': 'center',
                        # 'alignItems': 'center',
                    },
                )
                for i in range(10)
            ],
            layouts=[
                dict(
                    i=str(i),
                    x=i,
                    y=i + 1,
                    w=1,
                    h=i + i % 2 + 1,
                )
                for i in range(5)
            ],
            cols=5,
            rowHeight=75,
            placeholderBorderRadius='5px',
            margin=[5, 5],
            containerPadding=[8, 8],
            style={'border': '1px dashed #e1dfdd'},
        )
    ],
    style={'padding': 50},
)

if __name__ == '__main__':
    app.run(debug=True)
