import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import os
import uuid
from flask import request

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(id='output'),
        fuc.FefferyVditor(
            id='vditor',
            cdn='https://registry.npmmirror.com/vditor/3.10.4/files',
            height=600,
            toolbar=[
                "emoji",
                "headings",
                "bold",
                "italic",
                "strike",
                "link",
                "|",
                "list",
                "ordered-list",
                "check",
                "outdent",
                "indent",
                "|",
                "quote",
                "line",
                "code",
                "inline-code",
                "insert-before",
                "insert-after",
                "|",
                "upload",
                "record",
                "table",
                "|",
                "undo",
                "redo",
                "|",
                "fullscreen",
                "edit-mode",
                {
                    'name': "more",
                    'toolbar': [
                        "both",
                        "code-theme",
                        "content-theme",
                        "export",
                        "outline",
                        "preview"
                    ],
                },
            ],
            upload={
                'url': '/upload/',
                'extraData': {
                    'uploadId': str(uuid.uuid4())
                },
            },
        ),
        html.Pre('回显展示'),
        fuc.FefferyVditor(
            id='output-vditor',
            height=600,
            mode='wysiwyg',
            cdn='https://registry.npmmirror.com/vditor/3.10.4/files',
            preview={
                'markdown': {
                    'toc': True,
                    'mark': True,
                    'footnotes': True,
                    'autoSpace': True,
                },
                'math': {
                    'engine': 'KaTeX',
                    'inlineDigit': True,
                },
            },
            toolbarConfig={
                'pin': True,
            },
            counter={
                'enable': True,
                'type': 'text',
            },
            upload={
                'url': '/upload/',
                'extraData': {
                    'uploadId': str(uuid.uuid4())
                },
            },
        ),
    ],
    style={'padding': '50px'},
)


@app.callback(
    Output('output', 'children'),
    Input('vditor', 'wordCount'),
)
def show_word_count(wordCount):
    if wordCount:
        return wordCount
    return dash.no_update


@app.callback(
    Output('output-vditor', 'value'),
    Input('vditor', 'value'),
)
def show_value(value):
    if value:
        return value
    return dash.no_update


@app.server.route('/upload/', methods=['POST'])
def upload():
    """
    构建文件上传服务
    :return:
    """

    # 获取上传id参数，用于指向保存路径
    uploadId = request.values.get('uploadId')

    # 获取上传的文件名称
    filename = request.files['file[]'].filename

    # 基于上传id，若本地不存在则会自动创建目录
    try:
        os.makedirs(os.path.join('assets', uploadId))
    except FileExistsError:
        pass

    # 流式写出文件到指定目录
    with open(
        os.path.join('assets', uploadId, filename), 'wb'
    ) as f:
        # 流式写出大型文件，这里的10代表10MB
        for chunk in iter(
            lambda: request.files['file[]'].read(
                1024 * 1024 * 10
            ),
            b'',
        ):
            f.write(chunk)

    return {
        'msg': '上传成功',
        'code': 0,
        'data': {
            # "errFiles": [filename],
            'succMap': {
                f'{filename}': f'http://127.0.0.1:8050/assets/{uploadId}/{filename}',
            }
        },
    }


if __name__ == '__main__':
    app.run(debug=True)
