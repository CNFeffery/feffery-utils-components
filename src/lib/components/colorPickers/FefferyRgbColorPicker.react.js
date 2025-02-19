import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

/**
 * rgb色彩选择器FefferyRgbColorPicker
 */
const LazyFefferyRgbColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyRgbColorPicker.react'));

const FefferyRgbColorPicker = ({
    id,
    className,
    style,
    color = 'rgb(68, 206, 246)',
    showAlpha = false,
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyRgbColorPicker {
                ...{
                    id,
                    className,
                    style,
                    color,
                    showAlpha,
                    setProps,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyRgbColorPicker.propTypes = {
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
     * 监听或设置当前选中色彩对应rgb格式颜色值
     * 默认值：`'rgb(68, 206, 246)'`
     */
    color: PropTypes.string,

    /**
     * 是否显示透明度选择控件
     * 默认值：`false`
     */
    showAlpha: PropTypes.bool
};

export default FefferyRgbColorPicker;

export const propTypes = FefferyRgbColorPicker.propTypes;
export const defaultProps = FefferyRgbColorPicker.defaultProps;