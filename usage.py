import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        html.Div(
            html.Pre(
                '''
君不见黄河之水天上来，奔流到海不复回。
君不见高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。
烹羊宰牛且为乐，会须一饮三百杯。
岑夫子，丹丘生，将进酒，杯莫停。
与君歌一曲，请君为我倾耳听。
钟鼓馔玉不足贵，但愿长醉不愿醒。
古来圣贤皆寂寞，惟有饮者留其名。
陈王昔时宴平乐，斗酒十千恣欢谑。
主人何为言少钱，径须沽取对君酌。
五花马、千金裘，呼儿将出换美酒，与尔同销万古愁。
''',
                id='text-selection-target'
            ),
            id='text-selection-target-parent'
        ),
        fuc.FefferyTextSelection(
            id='text-selection-demo',
            # targetId='text-selection-target',
            targetType='selector',
            targetSelector='#text-selection-target-parent'
        ),
        html.Pre(
            id='text-selection-demo-output'
        )
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('text-selection-demo-output', 'children'),
    Input('text-selection-demo', 'selectedTextInfo')
)
def demo(selectedTextInfo):

    return json.dumps(
        selectedTextInfo,
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
