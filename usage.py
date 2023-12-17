import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import os
from flask import request, send_file

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Div(
            [
                fuc.FefferyImageCropper(
                    id='cropper',
                    src='https://raw.githubusercontent.com/roadmanfong/react-cropper/master/example/img/child.jpg',
                    aspectRatio=1,
                    dragMode='move',
                    cropBoxMovable=False,
                    cropBoxResizable=False,
                    preview='#img-preview',
                    style={
                        'width': '50%',
                        'height': '50%'
                    }
                ),
                html.Div(
                    id='img-preview',
                    style={
                        'margin': 'auto',
                        'width': '120px',
                        'height': '120px',
                        'overflow': 'hidden',
                        'float': 'left'
                    }
                ),
            ],
            style={
                'display': 'flex'
            }
        ),
        html.Div(
            [
                fuc.FefferyFancyButton(
                    '放大',
                    type='primary',
                    id='zoom1',
                    style={
                        'margin': 'auto',
                    }
                ),
                fuc.FefferyFancyButton(
                    '缩小',
                    type='primary',
                    id='zoom2',
                    style={
                        'margin': 'auto',
                    }
                ),
                fuc.FefferyFancyButton(
                    '逆时针旋转',
                    type='primary',
                    id='rotate1',
                    style={
                        'margin': 'auto',
                    }
                ),
                fuc.FefferyFancyButton(
                    '顺时针旋转',
                    type='primary',
                    id='rotate2',
                    style={
                        'margin': 'auto',
                    }
                ),
            ],
            style={
                'margin': '50px 500px',
                'display': 'flex'
            }
        ),
        html.Pre(id='output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    [Output('cropper', 'zoom'),
     Output('cropper', 'rotate')],
    [Input('zoom1', 'nClicks'),
     Input('zoom2', 'nClicks'),
     Input('rotate1', 'nClicks'),
     Input('rotate2', 'nClicks')],
    prevent_initial_call=True
)
def operate_cropper(zoom1, zoom2, rotate1, rotate2):
    trrigger_id = dash.ctx.triggered_id
    if trrigger_id == 'zoom1':
        return [{'isZoom': True, 'ratio': 0.1}, dash.no_update]
    elif trrigger_id == 'zoom2':
        return [{'isZoom': True, 'ratio': -0.1}, dash.no_update]
    elif trrigger_id == 'rotate1':
        return [dash.no_update, {'isRotate': True, 'degree': -90}]
    elif trrigger_id == 'rotate2':
        return [dash.no_update, {'isRotate': True, 'degree': 90}]
    else:
        return [dash.no_update, dash.no_update]


@app.callback(
    Output('output', 'children'),
    Input('cropper', 'croppedImageData'),
    [State('cropper', 'outputData'),
     State('cropper', 'containerData'),
     State('cropper', 'imageData'),
     State('cropper', 'canvasData'),
     State('cropper', 'cropBoxData')],
    prevent_initial_call=True
)
def render_output(croppedImageData, outputData, containerData, imageData, canvasData, cropBoxData):
    return [
        html.Img(src=croppedImageData, style={
            'width': '10%',
            'height': '10%'
        }),
        fuc.FefferyJsonViewer(
            id='json-viewer',
            data={
                'outputData': outputData,
                'containerData': containerData,
                'imageData': imageData,
                'canvasData': canvasData,
                'cropBoxData': cropBoxData
            }
        )
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
