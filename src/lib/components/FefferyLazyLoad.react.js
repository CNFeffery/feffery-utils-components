import React from 'react';
import LazyLoad from 'react-lazy-load';

// 定义懒加载容器组件FefferyLazyLoad
const FefferyLazyLoad = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
        height,
        width,
        offset,
        throttle,
        setProps,
        loading_state
    } = props;

    return (<LazyLoad
        id={id}
        style={style}
        className={className}
        height={height}
        width={width}
        throttle={throttle}
        offset={offset}
        onContentVisible={() => {
            setProps({
                visible: true
            })
        }}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >
        {children}
    </ LazyLoad>);
}

// 定义参数或属性
FefferyLazyLoad.propTypes = {
    // 部件id
    id: PropTypes.string,

    children: PropTypes.node,

    style: PropTypes.object,

    className: PropTypes.string,

    // 设置默认高度
    height: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    // 设置默认为宽度
    width: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.string
    ]),

    // 设置元素距离浏览器下边界若干像素距离时开始预加载
    // 默认为0
    offset: PropTypes.number,

    // 监听容器是否已出现在用户视图中
    visible: PropTypes.bool,

    // 设置节流所需的延时加载时长（单位：毫秒），默认为250
    throttle: PropTypes.number,

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
FefferyLazyLoad.defaultProps = {
    visible: false
}

export default React.memo(FefferyLazyLoad);