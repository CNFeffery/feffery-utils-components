import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdSwitch(
                    id='css-var-demo',
                    checked=False,
                    unCheckedChildren='🌞',
                    checkedChildren='🌛'
                ),

                fuc.FefferyCssVar(
                    id='css-var-demo-output'
                ),

                html.Div(
                    'FefferyCssVar示例',
                    style={
                        'background': 'var(--demo-bg-color)',
                        'color': 'var(--demo-color)',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'fontSize': '28px',
                        'transition': '0.2s',
                        'padding': '100px 150px'
                    }
                )
            ],
            direction='vertical'
        )
    ],
    style={
        'padding': '100px'
    }
)

@app.callback(
    Output('css-var-demo-output', 'cssVars'),
    Input('css-var-demo', 'checked')
)
def css_var_demo(checked):

    print(checked)

    if checked:
        return {
            '--demo-bg-color': 'black',
            '--demo-color': 'white'
        }

    return {
        '--demo-bg-color': 'white',
        '--demo-color': 'black'
    }

if __name__ == '__main__':
    app.run(debug=True)
