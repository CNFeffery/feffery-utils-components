# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyTiltHover(Component):
    """A FefferyTiltHover component.


Keyword arguments:

- id (string; optional):
    组件id.

- children (a list of or a singular dash component, string or number; optional):
    要进行倾斜悬浮效果编排的目标元素.

- className (string; optional):
    css类名.

- style (dict; optional):
    自定义css字典.

- key (string; optional):
    辅助刷新用唯一标识key值.

- tiltEnable (boolean; default True):
    设置是否启用倾斜效果，默认为True.

- tiltReverse (boolean; default False):
    设置是否反转倾斜方向，默认为False.

- tiltAngleXInitial (number; default 0):
    设置x轴上的初始倾斜值（度），默认为0.

- tiltAngleYInitial (number; default 0):
    设置y轴上的初始倾斜值（度），默认为0.

- tiltMaxAngleX (number; default 20):
    设置x轴上的的最大倾斜旋转（度），范围为0到90，默认为20.

- tiltMaxAngleY (number; default 20):
    设置y轴上的最大倾斜旋转（度），范围为0到90，默认为20.

- tiltAxis (a value equal to: 'x', 'y'; default undefined):
    启用单轴倾斜，可选值为'x'或'y'，默认为undefined.

- tiltAngleXManual (number; optional):
    设置在x轴上手动倾斜旋转（度），默认为None.

- tiltAngleYManual (number; optional):
    设置在y轴上手动倾斜旋转（度），默认为None.

- glareEnable (boolean; default False):
    设置是否启用眩光效果，默认为False.

- glareMaxOpacity (number; default 0.7):
    设置最大眩光不透明度，范围0到1，默认为0.7.

- glareColor (string; default '#ffffff'):
    设置眩光效果的颜色，默认为'#ffffff'.

- glareBorderRadius (string; default '0'):
    设置眩光效果的边框半径，接受任何标准的CSS边框半径。如果眩光颜色与页面颜色不同，则很有用，默认为'0'.

- glarePosition (a value equal to: 'top', 'right', 'bottom', 'left', 'all'; default 'bottom'):
    设置眩光效果的位置，可选的值为'top', 'right', 'bottom', 'left',
    'all'，默认为'bottom'.

- glareReverse (boolean; default False):
    设置是否反转眩光方向，默认为False.

- scale (number; default 1):
    设置组件的比例（1.5 = 150%，2 = 200%，等），默认为1.

- perspective (number; default 1000):
    定义对象（包装/子组件）与用户的距离。越低，倾斜度越大，默认为1000.

- flipVertically (boolean; default False):
    设置是否启用组件的垂直翻转，默认为False.

- flipHorizontally (boolean; default False):
    设置是否启用组件的水平翻转，默认为False.

- reset (boolean; default True):
    设置是否必须在事件中重置效果，默认为True.

- transitionEasing (string; default 'cubic-bezier(.03,.98,.52,.99)'):
    设置在操作组件时过渡效果，默认为'cubic-bezier(.03,.98,.52,.99)'.

- transitionSpeed (number; default 400):
    设置在操作组件时的过渡速度，默认为400.

- trackOnWindow (boolean; default False):
    设置是否跟踪整个窗口上的鼠标和触摸事件，默认为False.

- gyroscope (boolean; default False):
    设置是否启用设备方向检测，默认为False.

- listenMove (dict; optional):
    监听用户在组件上移动时触发的事件数据.

- listenEnter (dict; optional):
    监听用户进入组件时触发的事件数据.

- listenLeave (dict; optional):
    监听用户离开组件时触发的事件数据.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyTiltHover'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, tiltEnable=Component.UNDEFINED, tiltReverse=Component.UNDEFINED, tiltAngleXInitial=Component.UNDEFINED, tiltAngleYInitial=Component.UNDEFINED, tiltMaxAngleX=Component.UNDEFINED, tiltMaxAngleY=Component.UNDEFINED, tiltAxis=Component.UNDEFINED, tiltAngleXManual=Component.UNDEFINED, tiltAngleYManual=Component.UNDEFINED, glareEnable=Component.UNDEFINED, glareMaxOpacity=Component.UNDEFINED, glareColor=Component.UNDEFINED, glareBorderRadius=Component.UNDEFINED, glarePosition=Component.UNDEFINED, glareReverse=Component.UNDEFINED, scale=Component.UNDEFINED, perspective=Component.UNDEFINED, flipVertically=Component.UNDEFINED, flipHorizontally=Component.UNDEFINED, reset=Component.UNDEFINED, transitionEasing=Component.UNDEFINED, transitionSpeed=Component.UNDEFINED, trackOnWindow=Component.UNDEFINED, gyroscope=Component.UNDEFINED, listenMove=Component.UNDEFINED, listenEnter=Component.UNDEFINED, listenLeave=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'children', 'className', 'style', 'key', 'tiltEnable', 'tiltReverse', 'tiltAngleXInitial', 'tiltAngleYInitial', 'tiltMaxAngleX', 'tiltMaxAngleY', 'tiltAxis', 'tiltAngleXManual', 'tiltAngleYManual', 'glareEnable', 'glareMaxOpacity', 'glareColor', 'glareBorderRadius', 'glarePosition', 'glareReverse', 'scale', 'perspective', 'flipVertically', 'flipHorizontally', 'reset', 'transitionEasing', 'transitionSpeed', 'trackOnWindow', 'gyroscope', 'listenMove', 'listenEnter', 'listenLeave', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'children', 'className', 'style', 'key', 'tiltEnable', 'tiltReverse', 'tiltAngleXInitial', 'tiltAngleYInitial', 'tiltMaxAngleX', 'tiltMaxAngleY', 'tiltAxis', 'tiltAngleXManual', 'tiltAngleYManual', 'glareEnable', 'glareMaxOpacity', 'glareColor', 'glareBorderRadius', 'glarePosition', 'glareReverse', 'scale', 'perspective', 'flipVertically', 'flipHorizontally', 'reset', 'transitionEasing', 'transitionSpeed', 'trackOnWindow', 'gyroscope', 'listenMove', 'listenEnter', 'listenLeave', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FefferyTiltHover, self).__init__(children=children, **args)
