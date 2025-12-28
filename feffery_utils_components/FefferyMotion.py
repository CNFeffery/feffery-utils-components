# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class FefferyMotion(Component):
    """A FefferyMotion component.
动画编排组件FefferyMotion

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- children (a list of or a singular dash component, string or number; optional):
    组件型，要进行动画效果编排的目标元素.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- initial (dict | boolean | string; optional):
    设置当前组件初始化样式，传入`False`时用于禁用初始化动画，传入字符串时用于设置样式组别名.

- animate (dict | string; optional):
    设置从初始状态进行转化的目标样式，传入字符串时用于设置样式组别名.

- exit (dict | string; optional):
    设置当前元素从页面卸载时的目标样式，传入字符串时用于设置样式组别名.

- whileHover (dict | string; optional):
    设置鼠标悬停时的目标样式，传入字符串时用于设置样式组别名.

- whileTap (dict | string; optional):
    设置鼠标点按时的目标样式，传入字符串时用于设置样式组别名.

- transition (dict; optional):
    配置过渡动画相关参数  默认为：`{type: \"spring\", damping: 10, stiffness: 100}`.

    `transition` is a dict with keys:

    - delay (number; optional):
        设置过渡动画的开始延时时长，单位：秒  默认：`0`.

    - repeat (number | a value equal to: 'infinity'; optional):
        设置动画重复次数，特殊的，`'infinity'`表示无限循环.

    - repeatType (a value equal to: 'loop', 'reverse', 'mirror'; optional):
        设置动画的重复方式，可选的有`'loop'`、`'reverse'`、`'mirror'`.

    - repeatDelay (number; optional):
        设置动画每次重复的延时，单位：秒.

    - type (a value equal to: 'spring', 'tween'; optional):
        动画过渡类型，可选的有`'spring'`（弹簧运动型）、`'tween'`（补间型）  默认：'tween'.

    - duration (number; optional):
        设置过渡动画时长，单位：秒.

    - ease (a value equal to: 'linear', 'easeIn', 'easeOut', 'easeInOut', 'circIn', 'circOut', 'circInOut', 'backIn', 'backOut', 'backInOut', 'anticipate'; optional):
        `transition.type='tween'`时，用于设置过渡动画函数，可选的有`'linear'`、`'easeIn'`、`'easeOut'`、`'easeInOut'`、`'circIn'`、`'circOut'`、`'circInOut'`、`'backIn'`、`'backOut'`、`'backInOut'`、`'anticipate'`.

    - times (list of numbers; optional):
        针对分段过渡动画设置每段的时长比例，以`duration`为`1`单位.

- whileInView (dict | string; optional):
    设置当前组件进入视口后的目标样式，传入字符串时用于设置样式组别名.

- viewport (dict; optional):
    配置视口检测相关参数.

    `viewport` is a dict with keys:

    - once (boolean; optional):
        设置是否只进行一次视口检测，当设置为`True`时，当前元素进入视口后将维持`whileInView`所设置的样式
        默认：`False`.

    - margin (string; optional):
        设置用于辅助进行目标元素视口检测的外边界提前量，可设置例如`'200px'`统一为上右下左添加外边界，也可设置例如`'0px
        -20px 0px 100px'`分别控制不同方向  默认：`'0px'`.

    - amount (a value equal to: 'some', 'all'; optional):
        设置元素移入视口检测策略，设置为`'some'`时表示元素部分进入视口则视作进入，设置为`'all'`时表示元素全部进入视口才视作进入.

- variants (dict with strings as keys and values of type dict; optional):
    用于编排具有别名的样式组.

- animated (boolean; optional):
    监听当前组件的`animate`目标动画过程是否已完成.

- destroyWhenAnimated (boolean; default False):
    是否在动画完成后销毁当前组件  默认值：`False`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMotion'
    Transition = TypedDict(
        "Transition",
            {
            "delay": NotRequired[NumberType],
            "repeat": NotRequired[typing.Union[NumberType, Literal["infinity"]]],
            "repeatType": NotRequired[Literal["loop", "reverse", "mirror"]],
            "repeatDelay": NotRequired[NumberType],
            "type": NotRequired[Literal["spring", "tween"]],
            "duration": NotRequired[NumberType],
            "ease": NotRequired[Literal["linear", "easeIn", "easeOut", "easeInOut", "circIn", "circOut", "circInOut", "backIn", "backOut", "backInOut", "anticipate"]],
            "times": NotRequired[typing.Sequence[NumberType]]
        }
    )

    Viewport = TypedDict(
        "Viewport",
            {
            "once": NotRequired[bool],
            "margin": NotRequired[str],
            "amount": NotRequired[Literal["some", "all"]]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        initial: typing.Optional[typing.Union[dict, bool, str]] = None,
        animate: typing.Optional[typing.Union[dict, str]] = None,
        exit: typing.Optional[typing.Union[dict, str]] = None,
        whileHover: typing.Optional[typing.Union[dict, str]] = None,
        whileTap: typing.Optional[typing.Union[dict, str]] = None,
        transition: typing.Optional["Transition"] = None,
        whileInView: typing.Optional[typing.Union[dict, str]] = None,
        viewport: typing.Optional["Viewport"] = None,
        variants: typing.Optional[typing.Dict[typing.Union[str, float, int], dict]] = None,
        animated: typing.Optional[bool] = None,
        destroyWhenAnimated: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'children', 'style', 'className', 'initial', 'animate', 'exit', 'whileHover', 'whileTap', 'transition', 'whileInView', 'viewport', 'variants', 'animated', 'destroyWhenAnimated']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'children', 'style', 'className', 'initial', 'animate', 'exit', 'whileHover', 'whileTap', 'transition', 'whileInView', 'viewport', 'variants', 'animated', 'destroyWhenAnimated']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyMotion, self).__init__(children=children, **args)

setattr(FefferyMotion, "__init__", _explicitize_args(FefferyMotion.__init__))
