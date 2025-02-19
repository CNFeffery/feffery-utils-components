import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyTwitterColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyTwitterColorPicker.react'));

/**
 * Twitter风格色彩选择器FefferyGithubColorPicker
 */
const FefferyTwitterColorPicker = ({
    id,
    className,
    style,
    width = '276px',
    color,
    colors = ['#FF6900', '#FCB900', '#7BDCB5', '#00D084', '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7', '#9900EF'],
    triangle = 'top-left',
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyTwitterColorPicker {
                ...{
                    id,
                    className,
                    style,
                    width,
                    color,
                    colors,
                    triangle,
                    setProps,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyTwitterColorPicker.propTypes = {
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
     * 整体宽度
     * 默认值：`'276px'`
     */
    width: PropTypes.string,

    /**
     * 监听或设置当前选中色彩对应16进制颜色值
     */
    color: PropTypes.string,

    /**
     * 设置可选色彩对应16进制颜色值数组
     * 默认值：`['#FF6900', '#FCB900', '#7BDCB5', '#00D084', '#8ED1FC', '#0693E3', '#ABB8C3', '#EB144C', '#F78DA7', '#9900EF']`
     */
    colors: PropTypes.arrayOf(PropTypes.string),

    /**
     * 顶部箭头方位，可选项有`'hide'`、`'top-left'`、`'top-right'`
     * 默认值：`'top-left'`
     */
    triangle: PropTypes.oneOf(['hide', 'top-left', 'top-right'])
};

export default FefferyTwitterColorPicker;

export const propTypes = FefferyTwitterColorPicker.propTypes;
export const defaultProps = FefferyTwitterColorPicker.defaultProps;