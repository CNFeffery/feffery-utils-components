# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyPhotoSphereViewer(Component):
    """A FefferyPhotoSphereViewer component.


Keyword arguments:

- id (string; optional):
    组件id.

- height (string; optional):
    设置查看器高度，同css中的height属性.

- key (string; optional):
    辅助刷新用唯一标识key值.

- littlePlanet (boolean; default False):
    是否开启小星球模式  默认：False.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- src (string; optional):
    设置全景图片资源地址.

- width (string; optional):
    设置查看器宽度，同css中的width属性."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyPhotoSphereViewer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, src=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, littlePlanet=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'height', 'key', 'littlePlanet', 'loading_state', 'src', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'height', 'key', 'littlePlanet', 'loading_state', 'src', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyPhotoSphereViewer, self).__init__(**args)
