import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyEyeDropper = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyEyeDropper.react'));

/**
 * 色彩拾取组件FefferyEyeDropper
 */
const FefferyEyeDropper = ({
    id,
    enable = false,
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyEyeDropper {
                ...{
                    id,
                    enable,
                    setProps,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyEyeDropper.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 控制激活新一次的色彩拾取，每次完成色彩拾取后都会自动被重置为`false`
     * 默认值：`false`
     */
    enable: PropTypes.bool,

    /**
     * 监听最近一次色彩拾取操作对应16进制颜色值
     */
    color: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyEyeDropper;

export const propTypes = FefferyEyeDropper.propTypes;
export const defaultProps = FefferyEyeDropper.defaultProps;