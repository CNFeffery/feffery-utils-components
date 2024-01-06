import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

list_data = [{
    'title': '无缝滚动第一行无缝滚动第一行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第二行无缝滚动第二行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第三行无缝滚动第三行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第四行无缝滚动第四行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第五行无缝滚动第五行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第六行无缝滚动第六行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第七行无缝滚动第七行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第八行无缝滚动第八行',
    'date': '2017-12-16'
}, {
    'title': '无缝滚动第九行无缝滚动第九行',
    'date': '2017-12-16'
}]

app.layout = html.Div(
    [
        fuc.FefferySeamlessScroll(
            data=list_data,
            children=html.Ul(
                [
                    html.Li(
                        [
                            html.Span(
                                item['title'],
                            ),
                            html.Span(
                                item['date'],
                            )
                        ]
                    ) for item in list_data
                ]
            ),
            className='warp',
            classOption={
                # 'singleHeight': 30,
                # 'waitTime': 3000,
                'step': 0.3
            }
        ),
        fuc.FefferyStyle(
            rawStyle='''
            .warp {
                height: 270px;
                width: 360px;
                margin: 0 auto;
                overflow: hidden;
            }
            .warp ul {
                list-style: none;
                padding: 0;
                margin: 0 auto;
            }
            .warp ul li,
            a {
                display: block;
                height: 30px;
                line-height: 30px;
                display: flex;
                justify-content: space-between;
                font-size: 15px;
            }
            '''
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
