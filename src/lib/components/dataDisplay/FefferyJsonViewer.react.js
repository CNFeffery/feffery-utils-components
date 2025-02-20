import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyJsonViewer = React.lazy(() => import(/* webpackChunkName: "feffery_json_viewer" */ '../../fragments/dataDisplay/FefferyJsonViewer.react'));

/**
 * json数据展示组件FefferyJsonViewer
 */
const FefferyJsonViewer = ({
    rootName = false,
    indent = 4,
    theme = 'summerfruit:inverted',
    iconStyle = 'circle',
    collapsed = false,
    collapseStringsAfterLength = false,
    groupArraysAfterLength = 100,
    enableClipboard = true,
    displayObjectSize = true,
    displayDataTypes = true,
    editable = false,
    addible = false,
    deletable = false,
    sortKeys = false,
    quotesOnKeys = true,
    displayArrayKey = true,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyJsonViewer {
                ...{
                    rootName,
                    indent,
                    theme,
                    iconStyle,
                    collapsed,
                    collapseStringsAfterLength,
                    groupArraysAfterLength,
                    enableClipboard,
                    displayObjectSize,
                    displayDataTypes,
                    editable,
                    addible,
                    deletable,
                    sortKeys,
                    quotesOnKeys,
                    displayArrayKey,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyJsonViewer.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * `json`数据源
     */
    data: PropTypes.object,

    /**
     * 配置根节点键名，设置为`false`时不显示
     * 默认值：`false`
     */
    rootName: PropTypes.string,

    /**
     * 风格主题，可选项有`'apathy'`、`'apathy:inverted'`、`'ashes'`、`'bespin'`、`'brewer'`、
     * `'bright:inverted'`、`'bright'`、`'chalk'`、`'codeschool'`、`'colors'`、
     * `'eighties'`、`'embers'`、`'flat'`、`'google'`、`'grayscale'`、`'grayscale:inverted'`、
     * `'greenscreen'`、`'harmonic'`、`'hopscotch'`、`'isotope'`、`'marrakesh'`、`'mocha'`、
     * `'monokai'`、`'ocean'`、`'paraiso'`、`'pop'`、`'railscasts'`、`'rjv-default'`、
     * `'shapeshifter'`、`'shapeshifter:inverted'`、`'solarized'`、`'summerfruit'`、
     * `'summerfruit:inverted'`、`'threezerotwofour'`、`'tomorrow'`、`'tube'`、`'twilight'`
     * 默认值：`'summerfruit:inverted'`
     */
    theme: PropTypes.oneOf([
        'apathy', 'apathy:inverted', 'ashes', 'bespin', 'brewer',
        'bright:inverted', 'bright', 'chalk', 'codeschool', 'colors',
        'eighties', 'embers', 'flat', 'google', 'grayscale', 'grayscale:inverted',
        'greenscreen', 'harmonic', 'hopscotch', 'isotope', 'marrakesh', 'mocha',
        'monokai', 'ocean', 'paraiso', 'pop', 'railscasts', 'rjv-default',
        'shapeshifter', 'shapeshifter:inverted', 'solarized', 'summerfruit',
        'summerfruit:inverted', 'threezerotwofour', 'tomorrow', 'tube', 'twilight'
    ]),

    /**
     * 缩进空格数
     * 默认值：`4`
     */
    indent: PropTypes.number,

    /**
     * 辅助图标形状风格，可选项有`'circle'`、`'triangle'`、`'square'`
     * 默认值：`'circle'`
     */
    iconStyle: PropTypes.oneOf([
        'circle', 'triangle', 'square'
    ]),

    /**
     * 节点折叠行为，传入`bool`型时用于统一控制全部节点是否折叠，传入`int`型时用于设置节点展开的最大深度
     * 默认值：`false`
     */
    collapsed: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.number
    ]),

    /**
     * 针对超长字符串的省略展示行为，当传入`int`型时用于设置超长省略的截断字符长度
     * 默认值：`false`
     */
    collapseStringsAfterLength: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.number
    ]),

    /**
     * 针对数组元素，设置分组缩略展示的组内元素数量
     * 默认值：`100`
     */
    groupArraysAfterLength: PropTypes.number,

    /**
     * 是否开启复制到粘贴板快捷按钮
     * 默认值：`true`
     */
    enableClipboard: PropTypes.bool,

    /**
     * 是否开启元素尺寸展示
     * 默认值：`true`
     */
    displayObjectSize: PropTypes.bool,

    /**
     * 是否开启数据类型展示
     * 默认值：`true`
     */
    displayDataTypes: PropTypes.bool,

    /**
     * 是否开启编辑功能
     * 默认值：`false`
     */
    editable: PropTypes.bool,

    /**
     * 是否开启添加功能
     * 默认值：`false`
     */
    addible: PropTypes.bool,

    /**
     * 是否开启删除功能
     * 默认值：`false`
     */
    deletable: PropTypes.bool,

    /**
     * 是否按照键进行排序
     * 默认值：`false`
     */
    sortKeys: PropTypes.bool,

    /**
     * 是否对键添加引号包裹
     * 默认值：`true`
     */
    quotesOnKeys: PropTypes.bool,

    /**
     * 是否针对数组元素展示元素下标
     * 默认值：`true`
     */
    displayArrayKey: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyJsonViewer;

export const propTypes = FefferyJsonViewer.propTypes;
export const defaultProps = FefferyJsonViewer.defaultProps;