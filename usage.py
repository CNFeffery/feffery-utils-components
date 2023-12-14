import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import os
from flask import request, send_file

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyMarkdownEditor(
            id='markdown',
            toolbars={
                'toolbar': [
                    'bold',
                    'italic',
                    'underline',
                    'strikethrough',
                    'sub',
                    'sup',
                    'size',
                    'color',
                    '|',
                    'quote',
                    'detail',
                    'header',
                    'checklist',
                    'list',
                    'justify',
                    'panel',
                    '|',
                    'drawIo',
                    'graph',
                    {
                        'insert': ['image', 'audio', 'video', 'pdf', 'word', 'file', 'link', 'hr', 'br', 'code', 'formula', 'toc', 'table', 'ruby'],
                    },
                    '|',
                    'undo',
                    'redo',
                    'settings',
                    'codeTheme',
                    'export'
                ],
                'toolbarRight': ['fullScreen', '|'],
                'sidebar': ['mobilePreview', 'theme', 'copy'],
            },
            drawioIframeUrl='assets/drawio/drawio_demo.html',
            uploadConfig={
                'action': '/upload/',
                'headers': {
                    'test': '111'
                }
            },
            fineControl={
                'isOpen': True,
                'videoFineControlOptions': {
                    'isPoster': True,
                    'posterUrl': 'http://127.0.0.1:8050/get?filename=2dc5b01f-2bf5-4131-b883-30d384d7b3f1.png'
                }
            },
            style={
                'height': '800px'
            }
        ),
        html.Pre(id='output'),
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('output', 'children'),
    Input('markdown', 'value'),
    prevent_initial_call=True
)
def callback_output(value):
    return value


@app.server.route('/upload/', methods=['POST'])
def upload():
    '''
    构建文件上传服务
    :return:
    '''

    # 获取上传的文件名称
    filename = request.files['file'].filename

    # 基于上传id，若本地不存在则会自动创建目录
    try:
        os.mkdir(os.path.join('cache'))
    except FileExistsError:
        pass
    try:
        # 流式写出文件到指定目录
        with open(os.path.join('cache', filename), 'wb') as f:
            # 流式写出大型文件，这里的10代表10MB
            for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
                f.write(chunk)

        return {
            "errno": 0,
            "data": {
                "url": "http://127.0.0.1:8050/get?filename=" + filename,
                "alt": "yyy",
                "href": "zzz"
            }
        }
    except Exception as e:
        return {
            "errno": 1,
            "message": str(e)
        }


@app.server.route('/get', methods=['GET'])
def get_file():
    filename = request.args.get('filename')  # 从查询字符串中获取文件名
    # 检查文件是否存在，这里省略相关逻辑

    # 返回文件
    return send_file(os.path.join('cache', filename), as_attachment=True)


if __name__ == '__main__':
    app.run_server(debug=True)
