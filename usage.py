import json
import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyLocation(id='location'),
        html.Div(
            [
                dcc.Link(
                    '/page1',
                    href='/page1'
                ),

                dcc.Link(
                    '/page1#tag1',
                    href='/page1#tag1'
                ),

                dcc.Link(
                    '/page1?a=1&b=2',
                    href='/page1?a=1&b=2'
                )
            ],
            style={
                'display': 'flex',
                'gap': 8
            }
        ),

        html.Pre(id='output')
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('output', 'children'),
    [Input('location', 'href'),
     Input('location', 'pathname'),
     Input('location', 'search'),
     Input('location', 'hash'),
     Input('location', 'host'),
     Input('location', 'hostname'),
     Input('location', 'port'),
     Input('location', 'protocol'),
     Input('location', 'trigger')]
)
def demo(href,
         pathname,
         search,
         hash,
         host,
         hostname,
         port,
         protocol,
         trigger):

    return json.dumps(
        dict(
            href=href,
            pathname=pathname,
            search=search,
            hash=hash,
            host=host,
            hostname=hostname,
            port=port,
            protocol=protocol,
            trigger=trigger
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
