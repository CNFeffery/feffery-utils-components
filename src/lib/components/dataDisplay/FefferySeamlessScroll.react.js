import { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferySeamlessScroll = React.lazy(() => import(/* webpackChunkName: "feffery_seamless_scroll" */ '../../fragments/dataDisplay/FefferySeamlessScroll.react'));

/**
 * 无缝滚动组件FefferySeamlessScroll
 */
const FefferySeamlessScroll = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferySeamlessScroll {...props} />
        </Suspense>
    );
}

FefferySeamlessScroll.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，设置需要滚动展示的内容
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 组件型，左右切换时左切换区域内容
     */
    leftSwitchChildren: PropTypes.node,

    /**
     * 组件型，左右切换时右切换区域内容
     */
    rightSwitchChildren: PropTypes.node,

    /**
     * 无缝滚动对应列表数据
     */
    data: PropTypes.array.isRequired,

    /**
     * 配置功能
     */
    classOption: PropTypes.exact({
        /**
         * 滚动速度，数值越大速度滚动越快
         * 默认值：`1`
         */
        step: PropTypes.number,
        /**
         * 开启无缝滚动的数据量
         * 默认值：`5`
         */
        limitMoveNum: PropTypes.number,
        /**
         * 是否启用鼠标移入控制
         * 默认值：`true`
         */
        hoverStop: PropTypes.bool,
        /**
         * 方向，可选项有`0`（向下）、`1`（向上）、`2`（向左）、`3`（向右）
         * 默认值：`1`
         */
        direction: PropTypes.number,
        /**
         * 移动端是否开启触碰滑动
         * 默认值：`true`
         */
        openTouch: PropTypes.bool,
        /**
         * 单步运动停止的高度，`direction`为`0`、`1`时生效
         * 默认值：`0`
         */
        singleHeight: PropTypes.number,
        /**
         * 单步运动停止的宽度，`direction`为`2`、`3`时生效
         * 默认值：`0`
         */
        singleWidth: PropTypes.number,
        /**
         * 单步停止等待时间，单位：毫秒
         * 默认值：`1000`
         */
        waitTime: PropTypes.number,
        /**
         * 左右切换按钮距离左右边界的像素边距
         * 默认值：`30`
         */
        switchOffset: PropTypes.number,
        /**
         * 是否开启自动滚动
         * 默认值：`true`
         */
        autoPlay: PropTypes.bool,
        /**
         * 手动单步切换像素`step`值
         * 默认值：`134`
         */
        switchSingleStep: PropTypes.number,
        /**
         * 单步切换的动画时间，单位：毫秒
         * 默认值：`400`
         */
        switchDelay: PropTypes.number,
        /**
         * 不可点击状态对应控件父元素`css`类名
         * 默认值：`'disabled'`
         */
        switchDisabledClass: PropTypes.string,
        /**
         * `singleHeight`、`singleWidth`是否开启`rem`度量
         * 默认值：`false`
         */
        isSingleRemUnit: PropTypes.bool,
        /**
         * 左右方向的滚动是否显示控制器按钮，传入`true`时`autoPlay`将自动变为`false`
         * 默认值：`false`
         */
        navigation: PropTypes.bool,
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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

FefferySeamlessScroll.defaultProps = {
    classOption: {
        step: 1,
        limitMoveNum: 5,
        hoverStop: true,
        direction: 1,
        openTouch: true,
        singleHeight: 0,
        singleWidth: 0,
        waitTime: 1000,
        switchOffset: 30,
        autoPlay: true,
        switchSingleStep: 134,
        switchDelay: 400,
        switchDisabledClass: 'disabled',
        isSingleRemUnit: false,
        navigation: false
    }
}

export default FefferySeamlessScroll;

export const propTypes = FefferySeamlessScroll.propTypes;
export const defaultProps = FefferySeamlessScroll.defaultProps;