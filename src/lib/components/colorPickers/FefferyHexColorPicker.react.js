import PropTypes from 'prop-types';
import React, { Suspense } from 'react';

const LazyFefferyHexColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyHexColorPicker.react'));

/**
 * 16进制色彩选择器FefferyHexColorPicker
 */
const FefferyHexColorPicker = ({
    id,
    className,
    style,
    color = '#44cef6',
    showAlpha = false,
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyHexColorPicker {
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

FefferyHexColorPicker.propTypes = {
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
     * 默认值：`'#36a0f8'`
     */
    color: PropTypes.string,

    /**
     * 是否显示透明度选择控件
     * 默认值：`false`
     */
    showAlpha: PropTypes.bool
};

export default FefferyHexColorPicker;

export const propTypes = FefferyHexColorPicker.propTypes;
export const defaultProps = FefferyHexColorPicker.defaultProps;