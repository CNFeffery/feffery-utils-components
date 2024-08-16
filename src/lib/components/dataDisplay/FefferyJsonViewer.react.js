import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyJsonViewer = React.lazy(() => import(/* webpackChunkName: "feffery_json_viewer" */ '../../fragments/dataDisplay/FefferyJsonViewer.react'));

const FefferyJsonViewer = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyJsonViewer {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyJsonViewer.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 设置要展示的json数据
     */
    data: PropTypes.object,

    /**
     * 设置风格主题，可选的有'apathy'、'apathy:inverted'、'ashes'
     * 'bespin'、'brewer'、'bright:inverted'、'bright'、'chalk'
     * 'codeschool'、'colors'、'eighties'、'embers'、'flat'、'google'
     * 'grayscale'、'grayscale:inverted'、'greenscreen'、'harmonic'
     * 'hopscotch'、'isotope'、'marrakesh'、'mocha'、'monokai'、'ocean'
     * 'paraiso'、'pop'、'railscasts'、'rjv-default'、'shapeshifter'
     * 'shapeshifter:inverted'、'solarized'、'summerfruit'、'summerfruit:inverted'
     * 'threezerotwofour'、'tomorrow'、'tube'、'twilight'
     * 默认为'summerfruit:inverted'
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
     * 设置缩进空格数，默认为4
     */
    indent: PropTypes.number,

    /**
     * 设置辅助图标的形状风格，可选的有'circle'、'triangle'、'square'
     * 默认为'circle'
     */
    iconStyle: PropTypes.oneOf([
        'circle', 'triangle', 'square'
    ]),

    /**
     * 设置节点折叠行为，当传入bool型时用于统一控制全部节点折叠与否情况
     * 当传入整数时，用于设置节点展开的最大深度，默认为false
     */
    collapsed: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.number
    ]),

    /**
     * 用于设置针对超长字符串的省略展示行为，当传入整数时用于设置超长省略的截断字符长度
     * 默认为false
     */
    collapseStringsAfterLength: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.number
    ]),

    /**
     * 针对数组元素，设置分组缩略展示的组内元素数量，默认为100
     */
    groupArraysAfterLength: PropTypes.number,

    /**
     * 设置是否开启复制到粘贴板快捷按钮，默认为true
     */
    enableClipboard: PropTypes.bool,

    /**
     * 设置是否开启元素尺寸展示，默认为true
     */
    displayObjectSize: PropTypes.bool,

    /**
     * 设置是否开启数据类型展示，默认为true
     */
    displayDataTypes: PropTypes.bool,

    /**
     * 设置是否开启编辑功能，默认为false
     */
    editable: PropTypes.bool,

    /**
     * 设置是否开启添加功能，默认为false
     */
    addible: PropTypes.bool,

    /**
     * 设置是否开启删除功能，默认为false
     */
    deletable: PropTypes.bool,

    /**
     * 设置是否按照键进行排序，默认为false
     */
    sortKeys: PropTypes.bool,

    /**
     * 设置是否对键添加引号包裹，默认为true
     */
    quotesOnKeys: PropTypes.bool,

    /**
     * 设置是否针对数组元素展示元素下标，默认为true
     */
    displayArrayKey: PropTypes.bool,

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
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyJsonViewer.defaultProps = {
    indent: 4,
    theme: 'summerfruit:inverted',
    iconStyle: 'circle',
    collapsed: false,
    collapseStringsAfterLength: false,
    groupArraysAfterLength: 100,
    enableClipboard: true,
    displayObjectSize: true,
    displayDataTypes: true,
    editable: false,
    addible: false,
    deletable: false,
    sortKeys: false,
    quotesOnKeys: true,
    displayArrayKey: true
}

export default FefferyJsonViewer;

export const propTypes = FefferyJsonViewer.propTypes;
export const defaultProps = FefferyJsonViewer.defaultProps;