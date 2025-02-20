# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyDom2Image(Component):
    """A FefferyDom2Image component.
元素转图片组件FefferyDom2Image

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- targetSelector (string; optional):
    设置目标元素选择器，每次执行转换操作后都会重置为空值.

- scale (number; default 1):
    精度缩放比例  默认值：`1`.

- screenshotResult (dict; optional):
    监听最近一次元素转图片的结果数据.

    `screenshotResult` is a dict with keys:

    - selector (string; optional):
        记录本次转换结果对应的选择器.

    - status (a value equal to: 'success', 'failed'; optional):
        记录本次转换任务的执行状态，可选项有`'success'`、`'failed'`.

    - dataUrl (string; optional):
        若本次转换成功，则记录转换后的图片dataUrl信息.

    - timestamp (number; optional):
        对应当前任务完成的时间戳."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDom2Image'
    ScreenshotResult = TypedDict(
        "ScreenshotResult",
            {
            "selector": NotRequired[str],
            "status": NotRequired[Literal["success", "failed"]],
            "dataUrl": NotRequired[str],
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        targetSelector: typing.Optional[str] = None,
        scale: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        screenshotResult: typing.Optional["ScreenshotResult"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'targetSelector', 'scale', 'screenshotResult']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'targetSelector', 'scale', 'screenshotResult']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDom2Image, self).__init__(**args)
