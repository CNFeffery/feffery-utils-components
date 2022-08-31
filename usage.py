import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferySyntaxHighlighter(
            showLineNumbers=True,
            language='python',
            codeString="""
fac.AntdDivider(
    '默认linkTarget="_blank"',
    innerTextOrientation='left'
),
fmc.FefferyMarkdown(
    markdownStr='''[fac官网](http://fac.feffery.tech/)'''
),

fac.AntdDivider(
    'linkTarget="_self"',
    innerTextOrientation='left'
),
fmc.FefferyMarkdown(
    linkTarget='_self',
    markdownStr='''[fac官网](http://fac.feffery.tech/)'''
)
"""
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)
