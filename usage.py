
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyShadowDom(
            [
                fuc.FefferyStyle(
                    rawStyle='''
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#fce38a,#f38181);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
'''
                ),
                html.Div(
                    '节点1',
                    className='style-demo'
                )
            ]
        ),

        fuc.FefferyShadowDom(
            [
                fuc.FefferyStyle(
                    rawStyle='''
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#17ead9,#6078ea);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
'''
                ),
                html.Div(
                    '节点2',
                    className='style-demo'
                )
            ]
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
