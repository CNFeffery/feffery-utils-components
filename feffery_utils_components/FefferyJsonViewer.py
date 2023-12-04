# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyJsonViewer(Component):
    """A FefferyJsonViewer component.


Keyword arguments:

- id (string; optional):
    组件id.

- addible (boolean; default False):
    设置是否开启添加功能，默认为False.

- className (string | dict; optional):
    css类名.

- collapseStringsAfterLength (boolean | number; default False):
    用于设置针对超长字符串的省略展示行为，当传入整数时用于设置超长省略的截断字符长度  默认为False.

- collapsed (boolean | number; default False):
    设置节点折叠行为，当传入bool型时用于统一控制全部节点折叠与否情况  当传入整数时，用于设置节点展开的最大深度，默认为False.

- data (dict; optional):
    设置要展示的json数据.

- deletable (boolean; default False):
    设置是否开启删除功能，默认为False.

- displayArrayKey (boolean; default True):
    设置是否针对数组元素展示元素下标，默认为True.

- displayDataTypes (boolean; default True):
    设置是否开启数据类型展示，默认为True.

- displayObjectSize (boolean; default True):
    设置是否开启元素尺寸展示，默认为True.

- editable (boolean; default False):
    设置是否开启编辑功能，默认为False.

- enableClipboard (boolean; default True):
    设置是否开启复制到粘贴板快捷按钮，默认为True.

- groupArraysAfterLength (number; default 100):
    针对数组元素，设置分组缩略展示的组内元素数量，默认为100.

- iconStyle (a value equal to: 'circle', 'triangle', 'square'; default 'circle'):
    设置辅助图标的形状风格，可选的有'circle'、'triangle'、'square'  默认为'circle'.

- indent (number; default 4):
    设置缩进空格数，默认为4.

- key (string; optional):
    辅助刷新用唯一标识key值.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- quotesOnKeys (boolean; default True):
    设置是否对键添加引号包裹，默认为True.

- sortKeys (boolean; default False):
    设置是否按照键进行排序，默认为False.

- style (dict; optional):
    自定义css字典.

- theme (a value equal to: 'apathy', 'apathy:inverted', 'ashes', 'bespin', 'brewer', 'bright:inverted', 'bright', 'chalk', 'codeschool', 'colors', 'eighties', 'embers', 'flat', 'google', 'grayscale', 'grayscale:inverted', 'greenscreen', 'harmonic', 'hopscotch', 'isotope', 'marrakesh', 'mocha', 'monokai', 'ocean', 'paraiso', 'pop', 'railscasts', 'rjv-default', 'shapeshifter', 'shapeshifter:inverted', 'solarized', 'summerfruit', 'summerfruit:inverted', 'threezerotwofour', 'tomorrow', 'tube', 'twilight'; default 'summerfruit:inverted'):
    设置风格主题，可选的有'apathy'、'apathy:inverted'、'ashes'
    'bespin'、'brewer'、'bright:inverted'、'bright'、'chalk'
    'codeschool'、'colors'、'eighties'、'embers'、'flat'、'google'
    'grayscale'、'grayscale:inverted'、'greenscreen'、'harmonic'
    'hopscotch'、'isotope'、'marrakesh'、'mocha'、'monokai'、'ocean'
    'paraiso'、'pop'、'railscasts'、'rjv-default'、'shapeshifter'
    'shapeshifter:inverted'、'solarized'、'summerfruit'、'summerfruit:inverted'
    'threezerotwofour'、'tomorrow'、'tube'、'twilight'
    默认为'summerfruit:inverted'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyJsonViewer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, data=Component.UNDEFINED, theme=Component.UNDEFINED, indent=Component.UNDEFINED, iconStyle=Component.UNDEFINED, collapsed=Component.UNDEFINED, collapseStringsAfterLength=Component.UNDEFINED, groupArraysAfterLength=Component.UNDEFINED, enableClipboard=Component.UNDEFINED, displayObjectSize=Component.UNDEFINED, displayDataTypes=Component.UNDEFINED, editable=Component.UNDEFINED, addible=Component.UNDEFINED, deletable=Component.UNDEFINED, sortKeys=Component.UNDEFINED, quotesOnKeys=Component.UNDEFINED, displayArrayKey=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'addible', 'className', 'collapseStringsAfterLength', 'collapsed', 'data', 'deletable', 'displayArrayKey', 'displayDataTypes', 'displayObjectSize', 'editable', 'enableClipboard', 'groupArraysAfterLength', 'iconStyle', 'indent', 'key', 'loading_state', 'quotesOnKeys', 'sortKeys', 'style', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'addible', 'className', 'collapseStringsAfterLength', 'collapsed', 'data', 'deletable', 'displayArrayKey', 'displayDataTypes', 'displayObjectSize', 'editable', 'enableClipboard', 'groupArraysAfterLength', 'iconStyle', 'indent', 'key', 'loading_state', 'quotesOnKeys', 'sortKeys', 'style', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyJsonViewer, self).__init__(**args)
