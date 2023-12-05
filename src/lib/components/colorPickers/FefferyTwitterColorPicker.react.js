import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyTwitterColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyTwitterColorPicker.react'));

const FefferyTwitterColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyTwitterColorPicker {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyTwitterColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置组件整体宽度，默认为'276px'
    width: PropTypes.string,

    // 对应当前选中的16进制色彩字符串
    color: PropTypes.string,

    // 设置可选的16进制色彩值数组，默认为['#FF6900', '#FCB900', '#7BDCB5', '#00D084', '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7', '#9900EF']
    colors: PropTypes.arrayOf(PropTypes.string),

    // 设置顶部箭头的方位，可选的有'hide'、'top-left'、'top-right'，默认为'top-left'
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

// 设置默认参数
FefferyTwitterColorPicker.defaultProps = {
    triangle: 'top-left',
    width: '276px',
    colors: ['#FF6900', '#FCB900', '#7BDCB5', '#00D084', '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7', '#9900EF']
}

export default FefferyTwitterColorPicker;

export const propTypes = FefferyTwitterColorPicker.propTypes;
export const defaultProps = FefferyTwitterColorPicker.defaultProps;