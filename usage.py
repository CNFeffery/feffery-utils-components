
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            '鼠标移入此区域后进行图片粘贴',
            id='image-paste-container',
            shadow='hover-shadow',
            style={
                'height': '200px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'borderRadius': '6px',
                'border': '1px solid #f0f0f0',
                'marginBottom': '10px'
            }
        ),

        fuc.FefferyImagePaste(
            id='image-paste-demo',
            disabled=True
        ),

        html.Img(
            id='image-paste-output'
        )
    ],
    style={
        'padding': 25
    }
)

app.clientside_callback(
    '''(isHovering) => !isHovering;''',
    Output('image-paste-demo', 'disabled'),
    Input('image-paste-container', 'isHovering')
)


app.clientside_callback(
    '''(imageInfo) => imageInfo.base64;''',
    Output('image-paste-output', 'src'),
    Input('image-paste-demo', 'imageInfo'),
    prevent_initial_call=True
)


if __name__ == '__main__':
    app.run_server(debug=True)
