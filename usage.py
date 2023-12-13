import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

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


if __name__ == '__main__':
    app.run_server(debug=True)
