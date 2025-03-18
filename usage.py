import dash
import feffery_utils_components as fuc

app = dash.Dash(
    __name__,
    # 静态资源全量加载测试
    eager_loading=True,
)

app.layout = fuc.FefferyFancyButton('测试')

if __name__ == '__main__':
    app.run(debug=True)
