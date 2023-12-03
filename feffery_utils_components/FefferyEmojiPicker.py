# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyEmojiPicker(Component):
    """A FefferyEmojiPicker component.


Keyword arguments:

- id (string; optional):
    部件id.

- autoFocus (boolean; default False):
    设置选择器是否自动获取搜索框的焦点，默认为False.

- categories (list of a value equal to: 'frequent', 'people', 'nature', 'foods', 'activity', 'places', 'objects', 'symbols', 'flags's; default ['frequent', 'people', 'nature', 'foods', 'activity', 'places', 'objects', 'symbols', 'flags']):
    设置emoji显示的类别.

- className (string; optional):
    css类名.

- clickOutsideNums (number; default 0):
    监听点击选择器外区域的次数.

- custom (list of dicts; optional):
    设置是否显示搜索框，默认为True.

    `custom` is a list of dicts with keys:

    - emojis (list of dicts; optional):
        emoji分组的emoji.

        `emojis` is a list of dicts with keys:

        - id (string; optional):

            emoji的id.

        - keywords (list; optional):

            emoji的keywords.

        - name (string; optional):

            emoji的名称.

        - skins (list of dicts; optional):

            emoji的分类.

            `skins` is a list of dicts with keys:

            - src (string; optional):

                emoji的图片地址.

    - id (string; optional):
        emoji分组的id.

    - name (string; optional):
        emoji分组的名称.

- customCategoryIcons (dict; optional):
    设置是否显示搜索框，默认为True.

    `customCategoryIcons` is a dict with keys:

    - categoryIcons (dict; optional):
        自定义emoji分组的图标.

        `categoryIcons` is a dict with keys:

        - activity (dict; optional)

            `activity` is a dict with keys:

            - src (string; optional):
                自定义activity分组的src.

            - svg (string; optional):
                自定义activity分组的svg.

        - flags (dict; optional)

            `flags` is a dict with keys:

            - src (string; optional):
                自定义flags分组的src.

            - svg (string; optional):
                自定义flags分组的svg.

        - foods (dict; optional)

            `foods` is a dict with keys:

            - src (string; optional):
                自定义foods分组的src.

            - svg (string; optional):
                自定义foods分组的svg.

        - frequent (dict; optional):
            自定义frequent分组的icon.

            `frequent` is a dict with keys:

            - src (string; optional):
                自定义frequent分组的src.

            - svg (string; optional):
                自定义frequent分组的svg.

        - nature (dict; optional)

            `nature` is a dict with keys:

            - src (string; optional):
                自定义nature分组的src.

            - svg (string; optional):
                自定义nature分组的svg.

        - objects (dict; optional)

            `objects` is a dict with keys:

            - src (string; optional):
                自定义objects分组的src.

            - svg (string; optional):
                自定义objects分组的svg.

        - people (dict; optional)

            `people` is a dict with keys:

            - src (string; optional):
                自定义people分组的src.

            - svg (string; optional):
                自定义people分组的svg.

        - places (dict; optional)

            `places` is a dict with keys:

            - src (string; optional):
                自定义places分组的src.

            - svg (string; optional):
                自定义places分组的svg.

        - symbols (dict; optional)

            `symbols` is a dict with keys:

            - src (string; optional):
                自定义symbols分组的src.

            - svg (string; optional):
                自定义symbols分组的svg.

- dynamicWidth (boolean; default False):
    设置是否根据选择器的宽度动态计算每行显示的emoji数量，当设置为True时，perLine参数失效，默认为False.

- emojiButtonColors (list; optional):
    设置影响悬浮背景颜色的颜色数组.

- emojiButtonRadius (string; default '100%'):
    设置emoji按钮的圆角，默认为'100%'.

- emojiButtonSize (number; default 36):
    设置emoji按钮的大小，默认为36.

- emojiSize (number; default 24):
    设置emoji的大小，默认为24.

- emojiVersion (a value equal to: 1, 2, 3, 4, 5, 11, 12, 12.1, 13, 13.1, 14; default 14):
    设置使用的emoji数据的版本，默认为最新版14.

- exceptEmojis (list; optional):
    设置需要从选择器中移除的emoji的id.

- icons (a value equal to: 'auto', 'outline', 'solid'; default 'auto'):
    设置要用于选取器的图标类型。 outline用于浅色主题，solid用于深色主题.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'en', 'zh'; default 'zh'):
    语言设置.

- maxFrequentRows (number; default 0):
    设置要显示的frequent行的最大数目，设置为0将禁用frequent类别.

- navPosition (a value equal to: 'top', 'bottom', 'none'; default 'top'):
    设置导航栏的位置，默认为'top'.

- noResultsEmoji (string; default 'cry'):
    设置无结果时的emoji的id，默认为'cry'.

- perLine (number; default 9):
    设置每行显示的emoji数量，当dynamicWidth参数设置为True时，perLine参数失效，默认为9.

- previewEmoji (string; optional):
    设置当不悬停任何emoji时，用于预览的emoji的id。当预览位置位于底部时默认为'point_up'，当预览位置处于顶部时默认为'point_down'.

- previewPosition (a value equal to: 'top', 'bottom', 'none'; default 'bottom'):
    设置预览位置，默认为'bottom'.

- searchPosition (a value equal to: 'sticky', 'static', 'none'; default 'sticky'):
    设置搜索框的位置，默认为'sticky'.

- set (a value equal to: 'native', 'apple', 'facebook', 'google', 'twitter'; default 'native'):
    设置emoji的集合来源，默认为'native'，建议使用'native'.

- skin (a value equal to: 1, 2, 3, 4, 5, 6; default 1):
    设置emoji的皮肤类型，默认为1.

- skinTonePosition (a value equal to: 'preview', 'search', 'none'; default 'preview'):
    设置皮肤选择器的位置，默认为'preview'.

- style (dict; optional):
    自定义css字典.

- theme (a value equal to: 'auto', 'light', 'dark'; default 'auto'):
    设置选择器的主题，默认为'auto'.

- value (dict; optional):
    监听当前选择的emoji信息."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyEmojiPicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, locale=Component.UNDEFINED, categories=Component.UNDEFINED, custom=Component.UNDEFINED, customCategoryIcons=Component.UNDEFINED, autoFocus=Component.UNDEFINED, dynamicWidth=Component.UNDEFINED, perLine=Component.UNDEFINED, emojiButtonColors=Component.UNDEFINED, emojiButtonRadius=Component.UNDEFINED, emojiButtonSize=Component.UNDEFINED, emojiSize=Component.UNDEFINED, emojiVersion=Component.UNDEFINED, exceptEmojis=Component.UNDEFINED, icons=Component.UNDEFINED, maxFrequentRows=Component.UNDEFINED, navPosition=Component.UNDEFINED, noResultsEmoji=Component.UNDEFINED, previewEmoji=Component.UNDEFINED, previewPosition=Component.UNDEFINED, searchPosition=Component.UNDEFINED, set=Component.UNDEFINED, skin=Component.UNDEFINED, skinTonePosition=Component.UNDEFINED, theme=Component.UNDEFINED, value=Component.UNDEFINED, clickOutsideNums=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoFocus', 'categories', 'className', 'clickOutsideNums', 'custom', 'customCategoryIcons', 'dynamicWidth', 'emojiButtonColors', 'emojiButtonRadius', 'emojiButtonSize', 'emojiSize', 'emojiVersion', 'exceptEmojis', 'icons', 'loading_state', 'locale', 'maxFrequentRows', 'navPosition', 'noResultsEmoji', 'perLine', 'previewEmoji', 'previewPosition', 'searchPosition', 'set', 'skin', 'skinTonePosition', 'style', 'theme', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoFocus', 'categories', 'className', 'clickOutsideNums', 'custom', 'customCategoryIcons', 'dynamicWidth', 'emojiButtonColors', 'emojiButtonRadius', 'emojiButtonSize', 'emojiSize', 'emojiVersion', 'exceptEmojis', 'icons', 'loading_state', 'locale', 'maxFrequentRows', 'navPosition', 'noResultsEmoji', 'perLine', 'previewEmoji', 'previewPosition', 'searchPosition', 'set', 'skin', 'skinTonePosition', 'style', 'theme', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyEmojiPicker, self).__init__(**args)
