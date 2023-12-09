
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyHighlightWords(
            textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
            searchWords=['我们', '团结']
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
