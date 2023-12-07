# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyMotion(Component):
    """A FefferyMotion component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    要进行动画效果编排的目标元素.

- id (string; optional):
    组件id.

- animate (dict | string; optional):
    设置从初始状态进行转化的目标样式  传入字符串时用于设置样式组别名.

- className (string; optional):
    css类名.

- exit (dict | string; optional):
    设置当前元素从页面卸载时的目标样式  传入字符串时用于设置样式组别名.

- initial (dict | boolean | string; optional):
    设置当前组件初始化样式  传入False时用于禁用初始化动画  传入字符串时用于设置样式组别名.

- key (string; optional):
    强制刷新用.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional):
    css样式.

- transition (dict; optional):
    配置过渡动画相关参数  默认为：  {      type: \"spring\",      damping: 10,
    stiffness: 100  }.

    `transition` is a dict with keys:

    - delay (number; optional):
        设置过渡动画的开始延时时长，单位：秒  默认：0.

    - duration (number; optional):
        设置过渡动画时长，单位：秒.

    - ease (a value equal to: 'linear', 'easeIn', 'easeOut', 'easeInOut', 'circIn', 'circOut', 'circInOut', 'backIn', 'backOut', 'backInOut', 'anticipate'; optional):
        transition.type='tween'时，用于设置过渡动画函数，
        可选的有'linear'、'easeIn'、'easeOut'、'easeInOut'、'circIn'、
        'circOut'、'circInOut'、'backIn'、'backOut'、'backInOut'、'anticipate'.

    - repeat (number | a value equal to: 'infinity'; optional):
        设置动画重复次数，特殊的，'infinity'表示无限循环.

    - repeatDelay (number; optional):
        设置动画每次重复的延时，单位：秒.

    - repeatType (a value equal to: 'loop', 'reverse', 'mirror'; optional):
        设置动画的重复方式，可选的有'loop'、'reverse'、'mirror'.

    - times (list of numbers; optional):
        针对分段过渡动画设置每段的时长比例，以duration为1单位.

    - type (a value equal to: 'spring', 'tween'; optional):
        动画过渡类型，可选的有'spring'（弹簧运动型）、'tween'（补间型）  默认：'tween'.

- variants (dict with strings as keys and values of type dict; optional):
    用于编排具有别名的样式组.

- viewport (dict; optional):
    配置视口检测相关参数.

    `viewport` is a dict with keys:

    - amount (a value equal to: 'some', 'all'; optional):
        设置元素移入视口检测策略，设置为\"some\"时表示元素部分进入视口则视作进入，设置为\"all\"时表示元素全部进入视口才视作进入.

    - margin (string; optional):
        设置用于辅助进行目标元素视口检测的外边界提前量，可设置例如\"200px\"统一为上右下左添加外边界，也可设置例如\"0px
        -20px 0px 100px\"分别控制不同方向  默认：\"0px\".

    - once (boolean; optional):
        设置是否只进行一次视口检测，当设置为True时，当前元素进入视口后将维持whileInView所设置的样式
        默认：False.

- whileHover (dict | string; optional):
    设置鼠标悬停时的目标样式  传入字符串时用于设置样式组别名.

- whileInView (dict | string; optional):
    设置当前组件进入视口后的目标样式  传入字符串时用于设置样式组别名.

- whileTap (dict | string; optional):
    设置鼠标点按时的目标样式  传入字符串时用于设置样式组别名."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMotion'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, initial=Component.UNDEFINED, animate=Component.UNDEFINED, exit=Component.UNDEFINED, whileHover=Component.UNDEFINED, whileTap=Component.UNDEFINED, transition=Component.UNDEFINED, whileInView=Component.UNDEFINED, viewport=Component.UNDEFINED, variants=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'animate', 'className', 'exit', 'initial', 'key', 'loading_state', 'style', 'transition', 'variants', 'viewport', 'whileHover', 'whileInView', 'whileTap']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'animate', 'className', 'exit', 'initial', 'key', 'loading_state', 'style', 'transition', 'variants', 'viewport', 'whileHover', 'whileInView', 'whileTap']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyMotion, self).__init__(children=children, **args)
