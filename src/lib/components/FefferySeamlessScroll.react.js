import { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferySeamlessScroll = React.lazy(() => import(/* webpackChunkName: "feffery_seamless_scroll" */ '../fragments/FefferySeamlessScroll.react'));

const FefferySeamlessScroll = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferySeamlessScroll {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferySeamlessScroll.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 需要滚动展示的内容
     */
    children: PropTypes.node,

    /**
     * css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 左右切换时左切换区域内容
     */
    leftSwitchChildren: PropTypes.node,

    /**
     * 左右切换时右切换区域内容
     */
    rightSwitchChildren: PropTypes.node,

    /**
     * 无缝滚动list数据，组件内部只关注 data 数组的 length
     */
    data: PropTypes.array.isRequired,

    /**
     * 设置配置项
     */
    classOption: PropTypes.exact({
        /**
         * 设置滚动速度，数值越大速度滚动越快，默认为1。
         * step 值不建议太小,不然会有卡顿效果(如果设置了单步滚动,step需是单步大小的约数,否则无法保证单步滚动结束的位置是否准确。
         * 比如单步设置的 30,step 不能为 4)。
         */
        step: PropTypes.number,

        /**
         * 设置开启无缝滚动的数据量，默认为5
         * 默认：false
         */
        limitMoveNum: PropTypes.number,

        /**
         * 设置是否启用鼠标hover控制，默认为true
         */
        hoverStop: PropTypes.bool,

        /**
         * 设置方向: 0往下，1往上，2向左，3向右，默认为1
         */
        direction: PropTypes.number,

        /**
         * 设置移动端是否开启touch滑动，默认为true
         */
        openTouch: PropTypes.bool,

        /**
         * 设置单步运动停止的高度(默认值0是无缝不停止的滚动)，direction为0|1时生效，默认为0
         */
        singleHeight: PropTypes.number,

        /**
         * 设置单步运动停止的宽度(默认值0是无缝不停止的滚动)，direction为2|3时生效，默认为0
         */
        singleWidth: PropTypes.number,

        /**
         * 设置单步停止等待时间(默认值 1000ms)
         */
        waitTime: PropTypes.number,

        /**
         * 设置左右切换按钮距离左右边界的边距(px)，默认为30
         */
        switchOffset: PropTypes.number,

        /**
         * 是否开启自动滚动，默认为true
         */
        autoPlay: PropTypes.bool,

        /**
         * 设置手动单步切换step值(px)，默认为134
         */
        switchSingleStep: PropTypes.number,

        /**
         * 设置单步切换的动画时间(ms)，默认为400
         */
        switchDelay: PropTypes.number,

        /**
         * 设置不可以点击状态的switch按钮父元素的类名，默认为'disabled'
         */
        switchDisabledClass: PropTypes.string,

        /**
         * 设置singleHeight and singleWidth 是否开启rem度量，默认为false
         */
        isSingleRemUnit: PropTypes.bool,

        /**
         * 设置左右方向的滚动是否显示控制器按钮，true的时候autoPlay自动变为false，默认为false
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

// 设置默认参数
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