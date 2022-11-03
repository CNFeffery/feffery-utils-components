import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        *[
            fuc.FefferyDiv(
                enableClickAway=True,
                className={
                    '&:hover': {
                        'transform': 'translateX(20px)',
                        'cursor': 'pointer'
                    }
                },
                style={
                    'height': '100px',
                    'width': '100px',
                    'background': 'lightgrey',
                    'marginBottom': '20px'
                }
            )
            for i in range(200)
        ],
        fac.AntdBackTop(
            duration=1
        )
    ],
    style={
        'padding': '100px',
        'height': '10000px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
