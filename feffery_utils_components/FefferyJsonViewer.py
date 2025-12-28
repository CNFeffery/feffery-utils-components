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


class FefferyJsonViewer(Component):
    """A FefferyJsonViewer component.
json数据展示组件FefferyJsonViewer

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string | dict; optional):
    当前组件css类名.

- data (dict; optional):
    `json`数据源.

- rootName (string; default False):
    配置根节点键名，设置为`False`时不显示  默认值：`False`.

- theme (a value equal to: 'apathy', 'apathy:inverted', 'ashes', 'bespin', 'brewer', 'bright:inverted', 'bright', 'chalk', 'codeschool', 'colors', 'eighties', 'embers', 'flat', 'google', 'grayscale', 'grayscale:inverted', 'greenscreen', 'harmonic', 'hopscotch', 'isotope', 'marrakesh', 'mocha', 'monokai', 'ocean', 'paraiso', 'pop', 'railscasts', 'rjv-default', 'shapeshifter', 'shapeshifter:inverted', 'solarized', 'summerfruit', 'summerfruit:inverted', 'threezerotwofour', 'tomorrow', 'tube', 'twilight'; default 'summerfruit:inverted'):
    风格主题，可选项有`'apathy'`、`'apathy:inverted'`、`'ashes'`、`'bespin'`、`'brewer'`、
    `'bright:inverted'`、`'bright'`、`'chalk'`、`'codeschool'`、`'colors'`、
    `'eighties'`、`'embers'`、`'flat'`、`'google'`、`'grayscale'`、`'grayscale:inverted'`、
    `'greenscreen'`、`'harmonic'`、`'hopscotch'`、`'isotope'`、`'marrakesh'`、`'mocha'`、
    `'monokai'`、`'ocean'`、`'paraiso'`、`'pop'`、`'railscasts'`、`'rjv-default'`、
    `'shapeshifter'`、`'shapeshifter:inverted'`、`'solarized'`、`'summerfruit'`、
    `'summerfruit:inverted'`、`'threezerotwofour'`、`'tomorrow'`、`'tube'`、`'twilight'`
    默认值：`'summerfruit:inverted'`.

- indent (number; default 4):
    缩进空格数  默认值：`4`.

- iconStyle (a value equal to: 'circle', 'triangle', 'square'; default 'circle'):
    辅助图标形状风格，可选项有`'circle'`、`'triangle'`、`'square'`  默认值：`'circle'`.

- collapsed (boolean | number; default False):
    节点折叠行为，传入`bool`型时用于统一控制全部节点是否折叠，传入`int`型时用于设置节点展开的最大深度
    默认值：`False`.

- collapseStringsAfterLength (boolean | number; default False):
    针对超长字符串的省略展示行为，当传入`int`型时用于设置超长省略的截断字符长度  默认值：`False`.

- groupArraysAfterLength (number; default 100):
    针对数组元素，设置分组缩略展示的组内元素数量  默认值：`100`.

- enableClipboard (boolean; default True):
    是否开启复制到粘贴板快捷按钮  默认值：`True`.

- displayObjectSize (boolean; default True):
    是否开启元素尺寸展示  默认值：`True`.

- displayDataTypes (boolean; default True):
    是否开启数据类型展示  默认值：`True`.

- editable (boolean; default False):
    是否开启编辑功能  默认值：`False`.

- addible (boolean; default False):
    是否开启添加功能  默认值：`False`.

- deletable (boolean; default False):
    是否开启删除功能  默认值：`False`.

- sortKeys (boolean; default False):
    是否按照键进行排序  默认值：`False`.

- quotesOnKeys (boolean; default True):
    是否对键添加引号包裹  默认值：`True`.

- displayArrayKey (boolean; default True):
    是否针对数组元素展示元素下标  默认值：`True`."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyJsonViewer'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        data: typing.Optional[dict] = None,
        rootName: typing.Optional[str] = None,
        theme: typing.Optional[Literal["apathy", "apathy:inverted", "ashes", "bespin", "brewer", "bright:inverted", "bright", "chalk", "codeschool", "colors", "eighties", "embers", "flat", "google", "grayscale", "grayscale:inverted", "greenscreen", "harmonic", "hopscotch", "isotope", "marrakesh", "mocha", "monokai", "ocean", "paraiso", "pop", "railscasts", "rjv-default", "shapeshifter", "shapeshifter:inverted", "solarized", "summerfruit", "summerfruit:inverted", "threezerotwofour", "tomorrow", "tube", "twilight"]] = None,
        indent: typing.Optional[NumberType] = None,
        iconStyle: typing.Optional[Literal["circle", "triangle", "square"]] = None,
        collapsed: typing.Optional[typing.Union[bool, NumberType]] = None,
        collapseStringsAfterLength: typing.Optional[typing.Union[bool, NumberType]] = None,
        groupArraysAfterLength: typing.Optional[NumberType] = None,
        enableClipboard: typing.Optional[bool] = None,
        displayObjectSize: typing.Optional[bool] = None,
        displayDataTypes: typing.Optional[bool] = None,
        editable: typing.Optional[bool] = None,
        addible: typing.Optional[bool] = None,
        deletable: typing.Optional[bool] = None,
        sortKeys: typing.Optional[bool] = None,
        quotesOnKeys: typing.Optional[bool] = None,
        displayArrayKey: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'data', 'rootName', 'theme', 'indent', 'iconStyle', 'collapsed', 'collapseStringsAfterLength', 'groupArraysAfterLength', 'enableClipboard', 'displayObjectSize', 'displayDataTypes', 'editable', 'addible', 'deletable', 'sortKeys', 'quotesOnKeys', 'displayArrayKey']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'data', 'rootName', 'theme', 'indent', 'iconStyle', 'collapsed', 'collapseStringsAfterLength', 'groupArraysAfterLength', 'enableClipboard', 'displayObjectSize', 'displayDataTypes', 'editable', 'addible', 'deletable', 'sortKeys', 'quotesOnKeys', 'displayArrayKey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyJsonViewer, self).__init__(**args)

setattr(FefferyJsonViewer, "__init__", _explicitize_args(FefferyJsonViewer.__init__))
