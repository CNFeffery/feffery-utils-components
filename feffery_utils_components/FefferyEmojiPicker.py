# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyEmojiPicker(Component):
    """A FefferyEmojiPicker component.
emoji选择器组件FefferyEmojiPicker

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- locale (a value equal to: 'en', 'zh'; default 'zh'):
    语言设置，可选的有`'en'`、`'zh'`  默认值：'zh'.

- categories (list of a value equal to: 'frequent', 'people', 'nature', 'foods', 'activity', 'places', 'objects', 'symbols', 'flags's; default ['frequent', 'people', 'nature', 'foods', 'activity', 'places', 'objects', 'symbols', 'flags']):
    设置`emoji`显示的类别.

- custom (list of dicts; optional):
    设置是否显示搜索框  默认值：`True`.

    `custom` is a list of dicts with keys:

    - id (string; optional):
        emoji分组的id.

    - name (string; optional):
        emoji分组的名称.

    - emojis (list of dicts; optional):
        emoji分组的emoji.

        `emojis` is a list of dicts with keys:

        - id (string; optional):

            emoji的id.

        - name (string; optional):

            emoji的名称.

        - keywords (list; optional):

            emoji的keywords.

        - skins (list of dicts; optional):

            emoji的分类.

            `skins` is a list of dicts with keys:

            - src (string; optional):

                emoji的图片地址.

- customCategoryIcons (dict; optional):
    设置是否显示搜索框  默认值：`True`.

    `customCategoryIcons` is a dict with keys:

    - categoryIcons (dict; optional):
        自定义emoji分组的图标.

        `categoryIcons` is a dict with keys:

        - frequent (dict; optional):
            自定义frequent分组的icon.

            `frequent` is a dict with keys:

            - svg (string; optional):
                自定义frequent分组的svg.

            - src (string; optional):
                自定义frequent分组的src.

        - people (dict; optional)

            `people` is a dict with keys:

            - svg (string; optional):
                自定义people分组的svg.

            - src (string; optional):
                自定义people分组的src.

        - nature (dict; optional)

            `nature` is a dict with keys:

            - svg (string; optional):
                自定义nature分组的svg.

            - src (string; optional):
                自定义nature分组的src.

        - foods (dict; optional)

            `foods` is a dict with keys:

            - svg (string; optional):
                自定义foods分组的svg.

            - src (string; optional):
                自定义foods分组的src.

        - activity (dict; optional)

            `activity` is a dict with keys:

            - svg (string; optional):
                自定义activity分组的svg.

            - src (string; optional):
                自定义activity分组的src.

        - places (dict; optional)

            `places` is a dict with keys:

            - svg (string; optional):
                自定义places分组的svg.

            - src (string; optional):
                自定义places分组的src.

        - objects (dict; optional)

            `objects` is a dict with keys:

            - svg (string; optional):
                自定义objects分组的svg.

            - src (string; optional):
                自定义objects分组的src.

        - symbols (dict; optional)

            `symbols` is a dict with keys:

            - svg (string; optional):
                自定义symbols分组的svg.

            - src (string; optional):
                自定义symbols分组的src.

        - flags (dict; optional)

            `flags` is a dict with keys:

            - svg (string; optional):
                自定义flags分组的svg.

            - src (string; optional):
                自定义flags分组的src.

- autoFocus (boolean; default False):
    设置选择器是否自动获取搜索框的焦点  默认值：`False`.

- dynamicWidth (boolean; default False):
    设置是否根据选择器的宽度动态计算每行显示的emoji数量，当设置为`True`时，`perLine`参数失效
    默认值：`False`.

- perLine (number; default 9):
    设置每行显示的emoji数量，当`dynamicWidth`参数设置为`True`时，`perLine`参数失效  默认值：`9`.

- emojiButtonColors (list; optional):
    设置影响悬浮背景颜色的颜色数组.

- emojiButtonRadius (string; default '100%'):
    设置emoji按钮的圆角  默认值：`'100%'`.

- emojiButtonSize (number; default 36):
    设置emoji按钮的大小  默认值：`36`.

- emojiSize (number; default 24):
    设置emoji的大小  默认值：`24`.

- emojiVersion (a value equal to: 1, 2, 3, 4, 5, 11, 12, 12.1, 13, 13.1, 14; default 14):
    设置使用的emoji数据的版本，可选的有`1`、`2`、`3`、`4`、`5`、`11`、`12`、`12.1`、`13`、`13.1`、`14`
    默认为最新版`14`.

- exceptEmojis (list; optional):
    设置需要从选择器中移除的emoji的id.

- icons (a value equal to: 'auto', 'outline', 'solid'; default 'auto'):
    设置要用于选取器的图标类型，，可选的有`'auto'`、`'outline'`、`'solid'`，`'outline'`用于浅色主题，`'solid'`用于深色主题
    默认值：`'auto'`.

- maxFrequentRows (number; default 0):
    设置要显示的frequent行的最大数目，设置为`0`将禁用frequent类别.

- navPosition (a value equal to: 'top', 'bottom', 'none'; default 'top'):
    设置导航栏的位置，可选有`'top'`、`'bottom'`、`'none'`  默认值：`'top'`.

- noResultsEmoji (string; default 'cry'):
    设置无结果时的emoji的id  默认值：`'cry'`.

- previewEmoji (string; optional):
    设置当不悬停任何emoji时，用于预览的emoji的id，当预览位置位于底部时默认为`'point_up'`，当预览位置处于顶部时默认为`'point_down'`.

- previewPosition (a value equal to: 'top', 'bottom', 'none'; default 'bottom'):
    设置预览位置，可选有`'top'`、`'bottom'`、`'none'`  默认值：`'bottom'`.

- searchPosition (a value equal to: 'sticky', 'static', 'none'; default 'sticky'):
    设置搜索框的位置，可选的有`'sticky'`、`'static'`、`'none'`  默认值：`'sticky'`.

- set (a value equal to: 'native', 'apple', 'facebook', 'google', 'twitter'; default 'native'):
    设置emoji的集合来源，可选有`'native'`、`'apple'`、`'facebook'`、`'google'`、`'twitter'`，建议使用`'native'`
    默认值：`'native'`.

- skin (a value equal to: 1, 2, 3, 4, 5, 6; default 1):
    设置emoji的皮肤类型，可选有`1`、`2`、`3`、`4`、`5`、`6`  默认值：`1`.

- skinTonePosition (a value equal to: 'preview', 'search', 'none'; default 'preview'):
    设置皮肤选择器的位置，可选有`'preview'`、`'search'`、`'none'`  默认值：`'preview'`.

- theme (a value equal to: 'auto', 'light', 'dark'; default 'auto'):
    设置选择器的主题，可选的有`'auto'`、`'light'`、`'dark'`  默认值：`'auto'`.

- value (dict; optional):
    监听当前选择的emoji信息.

- clickOutsideNums (number; default 0):
    监听点击选择器外区域的次数."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyEmojiPicker'
    CustomEmojisSkins = TypedDict(
        "CustomEmojisSkins",
            {
            "src": NotRequired[str]
        }
    )

    CustomEmojis = TypedDict(
        "CustomEmojis",
            {
            "id": NotRequired[str],
            "name": NotRequired[str],
            "keywords": NotRequired[typing.Sequence],
            "skins": NotRequired[typing.Sequence["CustomEmojisSkins"]]
        }
    )

    Custom = TypedDict(
        "Custom",
            {
            "id": NotRequired[str],
            "name": NotRequired[str],
            "emojis": NotRequired[typing.Sequence["CustomEmojis"]]
        }
    )

    CustomCategoryIconsCategoryIconsFrequent = TypedDict(
        "CustomCategoryIconsCategoryIconsFrequent",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsPeople = TypedDict(
        "CustomCategoryIconsCategoryIconsPeople",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsNature = TypedDict(
        "CustomCategoryIconsCategoryIconsNature",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsFoods = TypedDict(
        "CustomCategoryIconsCategoryIconsFoods",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsActivity = TypedDict(
        "CustomCategoryIconsCategoryIconsActivity",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsPlaces = TypedDict(
        "CustomCategoryIconsCategoryIconsPlaces",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsObjects = TypedDict(
        "CustomCategoryIconsCategoryIconsObjects",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsSymbols = TypedDict(
        "CustomCategoryIconsCategoryIconsSymbols",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIconsFlags = TypedDict(
        "CustomCategoryIconsCategoryIconsFlags",
            {
            "svg": NotRequired[str],
            "src": NotRequired[str]
        }
    )

    CustomCategoryIconsCategoryIcons = TypedDict(
        "CustomCategoryIconsCategoryIcons",
            {
            "frequent": NotRequired["CustomCategoryIconsCategoryIconsFrequent"],
            "people": NotRequired["CustomCategoryIconsCategoryIconsPeople"],
            "nature": NotRequired["CustomCategoryIconsCategoryIconsNature"],
            "foods": NotRequired["CustomCategoryIconsCategoryIconsFoods"],
            "activity": NotRequired["CustomCategoryIconsCategoryIconsActivity"],
            "places": NotRequired["CustomCategoryIconsCategoryIconsPlaces"],
            "objects": NotRequired["CustomCategoryIconsCategoryIconsObjects"],
            "symbols": NotRequired["CustomCategoryIconsCategoryIconsSymbols"],
            "flags": NotRequired["CustomCategoryIconsCategoryIconsFlags"]
        }
    )

    CustomCategoryIcons = TypedDict(
        "CustomCategoryIcons",
            {
            "categoryIcons": NotRequired["CustomCategoryIconsCategoryIcons"]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        locale: typing.Optional[Literal["en", "zh"]] = None,
        categories: typing.Optional[typing.Sequence[Literal["frequent", "people", "nature", "foods", "activity", "places", "objects", "symbols", "flags"]]] = None,
        custom: typing.Optional[typing.Sequence["Custom"]] = None,
        customCategoryIcons: typing.Optional["CustomCategoryIcons"] = None,
        autoFocus: typing.Optional[bool] = None,
        dynamicWidth: typing.Optional[bool] = None,
        perLine: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        emojiButtonColors: typing.Optional[typing.Sequence] = None,
        emojiButtonRadius: typing.Optional[str] = None,
        emojiButtonSize: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        emojiSize: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        emojiVersion: typing.Optional[Literal[1, 2, 3, 4, 5, 11, 12, 12.1, 13, 13.1, 14]] = None,
        exceptEmojis: typing.Optional[typing.Sequence] = None,
        icons: typing.Optional[Literal["auto", "outline", "solid"]] = None,
        maxFrequentRows: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        navPosition: typing.Optional[Literal["top", "bottom", "none"]] = None,
        noResultsEmoji: typing.Optional[str] = None,
        previewEmoji: typing.Optional[str] = None,
        previewPosition: typing.Optional[Literal["top", "bottom", "none"]] = None,
        searchPosition: typing.Optional[Literal["sticky", "static", "none"]] = None,
        set: typing.Optional[Literal["native", "apple", "facebook", "google", "twitter"]] = None,
        skin: typing.Optional[Literal[1, 2, 3, 4, 5, 6]] = None,
        skinTonePosition: typing.Optional[Literal["preview", "search", "none"]] = None,
        theme: typing.Optional[Literal["auto", "light", "dark"]] = None,
        value: typing.Optional[dict] = None,
        clickOutsideNums: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'locale', 'categories', 'custom', 'customCategoryIcons', 'autoFocus', 'dynamicWidth', 'perLine', 'emojiButtonColors', 'emojiButtonRadius', 'emojiButtonSize', 'emojiSize', 'emojiVersion', 'exceptEmojis', 'icons', 'maxFrequentRows', 'navPosition', 'noResultsEmoji', 'previewEmoji', 'previewPosition', 'searchPosition', 'set', 'skin', 'skinTonePosition', 'theme', 'value', 'clickOutsideNums']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'locale', 'categories', 'custom', 'customCategoryIcons', 'autoFocus', 'dynamicWidth', 'perLine', 'emojiButtonColors', 'emojiButtonRadius', 'emojiButtonSize', 'emojiSize', 'emojiVersion', 'exceptEmojis', 'icons', 'maxFrequentRows', 'navPosition', 'noResultsEmoji', 'previewEmoji', 'previewPosition', 'searchPosition', 'set', 'skin', 'skinTonePosition', 'theme', 'value', 'clickOutsideNums']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyEmojiPicker, self).__init__(**args)
