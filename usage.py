
import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyMotion(
            style={
                'background': '#71afe5',
                'width': '50px',
                'height': '50px',
                'marginBottom': '10px'
            },
            animate={
                'transform': 'translateX(200px)',
                'background': '#d83b01'
            },
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2
            }
        ),

        fuc.FefferyMotion(
            '示例',
            style={
                'border': '1px dashed #71afe5',
                'width': '100px',
                'height': '100px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            animate={
                'transform': 'translateX(300px) rotate(180deg)',
                'borderRadius': '100%'
            },
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
