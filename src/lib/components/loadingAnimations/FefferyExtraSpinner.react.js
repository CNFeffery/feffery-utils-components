import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyExtraSpinner = React.lazy(() => import(/* webpackChunkName: "feffery_extra_spinner" */ '../../fragments/loadingAnimations/FefferyExtraSpinner.react'));

const FefferyExtraSpinner = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyExtraSpinner {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyExtraSpinner.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 加载动画类型
     */
    type: PropTypes.oneOf([
        "ball", "swap", "bars", "grid", "wave", "push", "firework",
        "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
        "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
        "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
        "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
    ]),

    /**
     * 设置尺寸
     */
    size: PropTypes.number,

    /**
     * 设置尺寸值单位，默认为'px'
     */
    sizeUnit: PropTypes.string,

    /**
     * 设置颜色
     */
    color: PropTypes.string,

    /**
     * 设置前景色
     */
    frontColor: PropTypes.string,

    /**
     * 设置背景色
     */
    backColor: PropTypes.string,

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
FefferyExtraSpinner.defaultProps = {
    sizeUnit: 'px',
    type: 'ball',
    color: '#1890ff',
    frontColor: '#def6ff',
    backColor: '#1890ff'
}

export default FefferyExtraSpinner;

export const propTypes = FefferyExtraSpinner.propTypes;
export const defaultProps = FefferyExtraSpinner.defaultProps;