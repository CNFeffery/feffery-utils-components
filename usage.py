import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import os
from flask import request, send_file

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyRichTextEditor(
            id='editor',
            editorStyle={
                'height': '500px'
            },
            uploadImage={
                'server': '/upload/',
                'fieldName': 'file',
                # 'maxFileSize': 2
            },
            uploadVideo={
               'server': '/upload/',
               'fieldName': 'file',
            #    'maxFileSize': 10
            }
        ),
        html.Pre(id='output-html'),
        html.Pre(id='output-text'),
    ],
    id='app-container',
    style={
        'width': '50%', 
        'margin': '25px auto'
    }
)


@app.callback(
    Output('output-html', 'children'),
    Input('editor', 'htmlValue'),
    prevent_initial_call=True
)
def callback_output(htmlValue):
    return htmlValue


@app.callback(
    Output('output-text', 'children'),
    Input('editor', 'textValue'),
    prevent_initial_call=True
)
def callback_output(textValue):
    return textValue


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
