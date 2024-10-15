import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyExtraSpinner = React.lazy(() => import(/* webpackChunkName: "feffery_extra_spinner" */ '../../fragments/loadingAnimations/FefferyExtraSpinner.react'));

/**
 * 额外加载动画组件FefferyExtraSpinner
 */
const FefferyExtraSpinner = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyExtraSpinner {...props} />
        </Suspense>
    );
}

FefferyExtraSpinner.propTypes = {
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
     * 可用的动画类型，可选项有`'ball'`、`'swap'`、`'bars'`、`'grid'`、`'wave'`、`'push'`、`'firework'`、
     * `'stage'`、`'ring'`、`'heart'`、`'guard'`、`'rotate'`、`'spiral'`、`'pulse'`、`'swish'`、
     * `'sequence'`、`'impulse'`、`'cube'`、`'magic'`、`'flag'`、`'fill'`、`'sphere'`、`'domino'`、
     * `'goo'`、`'comb'`、`'pong'`、`'rainbow'`、`'hoop'`、`'flapper'`、`'jellyfish'`、`'trace'`、
     * `'classic'`、`'whisper'`、`'metro'`
     */
    type: PropTypes.oneOf([
        "ball", "swap", "bars", "grid", "wave", "push", "firework",
        "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
        "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
        "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
        "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
    ]),

    /**
     * 图标尺寸值
     */
    size: PropTypes.number,

    /**
     * 图标尺寸值单位
     * 默认值：`'px'`
     */
    sizeUnit: PropTypes.string,

    /**
     * 图标颜色
     */
    color: PropTypes.string,

    /**
     * 图标前景色
     */
    frontColor: PropTypes.string,

    /**
     * 图标背景色
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