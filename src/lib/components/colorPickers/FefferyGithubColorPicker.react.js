import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGithubColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyGithubColorPicker.react'));

/**
 * Github风格色彩选择器FefferyGithubColorPicker
 */
const FefferyGithubColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGithubColorPicker {...props} />
        </Suspense>
    );
}

FefferyGithubColorPicker.propTypes = {
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
    className: PropTypes.string,

    /**
     * 监听或设置当前选中色彩对应16进制颜色值
     */
    color: PropTypes.string,

    /**
     * 设置可选色彩对应16进制颜色值数组
     * 默认值：`['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB']`
     */
    colors: PropTypes.arrayOf(PropTypes.string),

    /**
     * 顶部箭头方位，可选项有`'hide'`、`'top-left'`、`'top-right'`
     * 默认值：`'top-left'`
     */
    triangle: PropTypes.oneOf(['hide', 'top-left', 'top-right']),

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
    })
};

FefferyGithubColorPicker.defaultProps = {
    triangle: 'top-left',
    colors: ['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB']
}

export default FefferyGithubColorPicker;

export const propTypes = FefferyGithubColorPicker.propTypes;
export const defaultProps = FefferyGithubColorPicker.defaultProps;