if True:
    import sys

    sys.path.append('../../')
    import dash
    import time
    from dash import html
    from flask import Response, request
    import feffery_utils_components as fuc
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)


@app.server.route('/stream', methods=['POST'])
def stream():
    print('headers: {}'.format(request.headers))
    print(
        'body：', eval(request.get_data().decode('utf-8'))
    )
    print('cookies: ', request.cookies)

    def _stream():
        for i in range(999):
            time.sleep(0.5)
            yield 'data: {}\n\n'.format(time.time())

    return Response(_stream(), mimetype='text/event-stream')


app.layout = html.Div(
    [
        fuc.FefferyPostEventSource(
            url='/stream',
            headers={
                'test-header': 'FefferyPostEventSource'
            },
            body='{"test": 999}',
        )
    ],
    style=style(padding=100),
)

if __name__ == '__main__':
    app.run(debug=True)
