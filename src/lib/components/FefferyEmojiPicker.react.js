import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyEmojiPicker = React.lazy(() => import(/* webpackChunkName: "feffery_emoji_picker" */ '../fragments/FefferyEmojiPicker.react'));

const FefferyEmojiPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyEmojiPicker {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyEmojiPicker.propTypes = {
    /**
     * 部件id
     */
    id: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 语言设置
     */
    locale: PropTypes.oneOf(['en', 'zh']),

    /**
     * 设置emoji显示的类别
     */
    categories: PropTypes.arrayOf(PropTypes.oneOf(['frequent', 'people', 'nature', 'foods', 'activity', 'places', 'objects', 'symbols', 'flags'])),

    /**
     * 设置是否显示搜索框，默认为true
     */
    custom: PropTypes.arrayOf(PropTypes.exact({
        /**
         * emoji分组的id
         */
        id: PropTypes.string,
        /**
         * emoji分组的名称
         */
        name: PropTypes.string,
        /**
         * emoji分组的emoji
         */
        emojis: PropTypes.arrayOf(
            PropTypes.exact({
                /**
                 * emoji的id
                 */
                id: PropTypes.string,
                /**
                 * emoji的名称
                 */
                name: PropTypes.string,
                /**
                 * emoji的keywords
                 */
                keywords: PropTypes.array,
                /**
                 * emoji的分类
                 */
                skins: PropTypes.arrayOf(
                    PropTypes.shape({
                        /**
                         * emoji的图片地址
                         */
                        src: PropTypes.string,
                    })
                )
            })
        ),
    })),

    /**
     * 设置是否显示搜索框，默认为true
     */
    customCategoryIcons : PropTypes.shape({
        /**
         * 自定义emoji分组的图标
         */
        categoryIcons: PropTypes.shape({
            /**
             * 自定义frequent分组的icon
             */
            frequent: PropTypes.shape({
                /**
                 * 自定义frequent分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义frequent分组的src
                 */
                src: PropTypes.string,
            }),
            people: PropTypes.shape({
                /**
                 * 自定义people分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义people分组的src
                 */
                src: PropTypes.string,
            }),
            nature: PropTypes.shape({
                /**
                 * 自定义nature分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义nature分组的src
                 */
                src: PropTypes.string,
            }),
            foods: PropTypes.shape({
                /**
                 * 自定义foods分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义foods分组的src
                 */
                src: PropTypes.string,
            }),
            activity: PropTypes.shape({
                /**
                 * 自定义activity分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义activity分组的src
                 */
                src: PropTypes.string,
            }),
            places: PropTypes.shape({
                /**
                 * 自定义places分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义places分组的src
                 */
                src: PropTypes.string,
            }),
            objects: PropTypes.shape(
                {
                    /**
                     * 自定义objects分组的svg
                     */
                    svg: PropTypes.string,
                    /**
                     * 自定义objects分组的src
                     */
                    src: PropTypes.string,
                }
            ),
            symbols: PropTypes.shape({
                /**
                 * 自定义symbols分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义symbols分组的src
                 */
                src: PropTypes.string,
            }),
            flags: PropTypes.shape({
                /**
                 * 自定义flags分组的svg
                 */
                svg: PropTypes.string,
                /**
                 * 自定义flags分组的src
                 */
                src: PropTypes.string,
            })
        })
    }),

    /**
     * 设置选择器是否自动获取搜索框的焦点，默认为false
     */
    autoFocus: PropTypes.bool,

    /**
     * 设置是否根据选择器的宽度动态计算每行显示的emoji数量，当设置为true时，perLine参数失效，默认为false
     */
    dynamicWidth: PropTypes.bool,

    /**
     * 设置每行显示的emoji数量，当dynamicWidth参数设置为true时，perLine参数失效，默认为9
     */
    perLine: PropTypes.number,

    /**
     * 设置影响悬浮背景颜色的颜色数组
     */
    emojiButtonColors: PropTypes.array,

    /**
     * 设置emoji按钮的圆角，默认为'100%'
     */
    emojiButtonRadius: PropTypes.string,

    /**
     * 设置emoji按钮的大小，默认为36
     */
    emojiButtonSize: PropTypes.number,

    /**
     * 设置emoji的大小，默认为24
     */
    emojiSize: PropTypes.number,

    /**
     * 设置使用的emoji数据的版本，默认为最新版14
     */
    emojiVersion: PropTypes.oneOf([1, 2, 3, 4, 5, 11, 12, 12.1, 13, 13.1, 14]),

    /**
     * 设置需要从选择器中移除的emoji的id
     */
    exceptEmojis: PropTypes.array,

    /**
     * 设置要用于选取器的图标类型。 outline用于浅色主题，solid用于深色主题
     */
    icons: PropTypes.oneOf(['auto', 'outline', 'solid']),

    /**
     * 设置要显示的frequent行的最大数目，设置为0将禁用frequent类别
     */
    maxFrequentRows: PropTypes.number,

    /**
     * 设置导航栏的位置，默认为'top'
     */
    navPosition: PropTypes.oneOf(['top', 'bottom', 'none']),

    /**
     * 设置无结果时的emoji的id，默认为'cry'
     */
    noResultsEmoji: PropTypes.string,

    /**
     * 设置当不悬停任何emoji时，用于预览的emoji的id。当预览位置位于底部时默认为'point_up'，当预览位置处于顶部时默认为'point_down'
     */
    previewEmoji: PropTypes.string,

    /**
     * 设置预览位置，默认为'bottom'
     */
    previewPosition: PropTypes.oneOf(['top', 'bottom', 'none']),

    /**
     * 设置搜索框的位置，默认为'sticky'
     */
    searchPosition: PropTypes.oneOf(['sticky', 'static', 'none']),

    /**
     * 设置emoji的集合来源，默认为'native'，建议使用'native'
     */
    set: PropTypes.oneOf(['native', 'apple', 'facebook', 'google', 'twitter']),

    /**
     * 设置emoji的皮肤类型，默认为1
     */
    skin: PropTypes.oneOf([1, 2, 3, 4, 5, 6]),

    /**
     * 设置皮肤选择器的位置，默认为'preview'
     */
    skinTonePosition: PropTypes.oneOf(['preview', 'search', 'none']),

    /**
     * 设置选择器的主题，默认为'auto'
     */
    theme: PropTypes.oneOf(['auto', 'light', 'dark']),

    /**
     * 监听当前选择的emoji信息
     */
    value: PropTypes.object,

    /**
     * 监听点击选择器外区域的次数
     */
    clickOutsideNums: PropTypes.number,

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 设置默认参数
FefferyEmojiPicker.defaultProps = {
    locale: 'zh',
    categories: ['frequent', 'people', 'nature', 'foods', 'activity', 'places', 'objects', 'symbols', 'flags'],
    autoFocus: false,
    dynamicWidth: false,
    perLine: 9,
    emojiButtonColors: [],
    emojiButtonRadius: '100%',
    emojiButtonSize: 36,
    emojiSize: 24,
    emojiVersion: 14,
    exceptEmojis: [],
    icons: 'auto',
    maxFrequentRows: 0,
    navPosition: 'top',
    noResultsEmoji: 'cry',
    previewPosition: 'bottom',
    searchPosition:'sticky',
    set: 'native',
    skin: 1,
    skinTonePosition: 'preview',
    theme: 'auto',
    clickOutsideNums: 0
}

export default FefferyEmojiPicker;

export const propTypes = FefferyEmojiPicker.propTypes;
export const defaultProps = FefferyEmojiPicker.defaultProps;