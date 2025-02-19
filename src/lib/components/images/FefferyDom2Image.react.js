import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyDom2Image = React.lazy(() => import(/* webpackChunkName: "feffery_dom2image" */ '../../fragments/images/FefferyDom2Image.react'));

/**
 * 元素转图片组件FefferyDom2Image
 */
const FefferyDom2Image = ({
    scale = 1,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyDom2Image {
                ...{
                    scale,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyDom2Image.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置目标元素选择器，每次执行转换操作后都会重置为空值
     */
    targetSelector: PropTypes.string,

    /**
     * 精度缩放比例
     * 默认值：`1`
     */
    scale: PropTypes.number,

    /**
     * 监听最近一次元素转图片的结果数据
     */
    screenshotResult: PropTypes.exact({
        /**
         * 记录本次转换结果对应的选择器
         */
        selector: PropTypes.string,
        /**
         * 记录本次转换任务的执行状态，可选项有`'success'`、`'failed'`
         */
        status: PropTypes.oneOf(['success', 'failed']),
        /**
         * 若本次转换成功，则记录转换后的图片dataUrl信息
         */
        dataUrl: PropTypes.string,
        /**
         * 对应当前任务完成的时间戳
         */
        timestamp: PropTypes.number
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyDom2Image;

export const propTypes = FefferyDom2Image.propTypes;
export const defaultProps = FefferyDom2Image.defaultProps;