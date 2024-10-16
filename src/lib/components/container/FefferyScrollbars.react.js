// react核心
import PropTypes from 'prop-types';
// 组件核心
import SimpleBarReact from "simplebar-react";
// 样式
import "simplebar/src/simplebar.css";

/**
 * 滚动条容器组件FefferyScrollbars
 */
const FefferyScrollbars = (props) => {
    const {
        id,
        children,
        style,
        className,
        key,
        autoHide,
        classNames,
        forceVisible,
        timeout,
        scrollbarMinSize,
        scrollbarMaxSize,
        loading_state
    } = props;

    return <SimpleBarReact
        id={id}
        style={style}
        className={className}
        key={key}
        autoHide={autoHide}
        classNames={classNames}
        forceVisible={forceVisible}
        timeout={timeout}
        scrollbarMinSize={scrollbarMinSize}
        scrollbarMaxSize={scrollbarMaxSize}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >
        {children}
    </ SimpleBarReact>;
}

FefferyScrollbars.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 是否在无操作时自动隐藏滚动条
     * 默认值：`true`
     */
    autoHide: PropTypes.bool,

    /**
     * 各组成部分css类名
     */
    classNames: PropTypes.exact({
        /**
         * 内容区域容器
         */
        content: PropTypes.string,
        /**
         * 正在滚动的内容容器
         */
        scrollContent: PropTypes.string,
        /**
         * 滚动条
         */
        scrollbar: PropTypes.string,
        /**
         * 滚动条滑块
         */
        track: PropTypes.string
    }),

    /**
     * 滑块区域是否强制可见，可传入由`'x'`、`'y'`组成的列表进行水平、竖直方向的单独设置
     * 默认值：`false`
     */
    forceVisible: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.oneOf(['x', 'y'])
    ]),

    /**
     * 滑块自动隐藏延时，单位：毫秒
     * 默认值：`1000`
     */
    timeout: PropTypes.number,

    /**
     * 滚动条最小像素长度
     * 默认值：`25`
     */
    scrollbarMinSize: PropTypes.number,

    /**
     * 滚动条最大像素长度
     */
    scrollbarMaxSize: PropTypes.number,

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

FefferyScrollbars.defaultProps = {
    autoHide: true,
    timeout: 1000,
    scrollbarMinSize: 25,
    forceVisible: false
}

export default FefferyScrollbars;