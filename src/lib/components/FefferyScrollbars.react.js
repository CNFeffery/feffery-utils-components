import SimpleBarReact from "simplebar-react";
import "simplebar/src/simplebar.css";
import PropTypes from 'prop-types';

// 定义自定义滚动条容器组件FefferyScrollbars
const FefferyScrollbars = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
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


// 定义参数或属性
FefferyScrollbars.propTypes = {
    // 组件id
    id: PropTypes.string,

    children: PropTypes.node,

    style: PropTypes.object,

    className: PropTypes.string,

    // 设置是否在无操作时自动隐藏滚动条，默认为true
    autoHide: PropTypes.bool,

    // 针对各组成部分单独设置自定义css类名
    classNames: PropTypes.exact({
        // 内容区域容器
        content: PropTypes.string,
        // 正在滚动的内容容器
        scrollContent: PropTypes.string,
        // 滚动条
        scrollbar: PropTypes.string,
        // 滚动条滑块
        track: PropTypes.string
    }),

    // 设置滑块区域是否强制可见，默认为false
    forceVisible: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.oneOf(['x', 'y'])
    ]),

    // 设置滑块自动隐藏的毫秒数，默认为1000
    timeout: PropTypes.number,

    // 设置滚动条最小像素长度，默认为25
    scrollbarMinSize: PropTypes.number,

    // 设置滚动条最大像素长度，默认无限制
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

// 设置默认参数
FefferyScrollbars.defaultProps = {
    autoHide: true,
    timeout: 1000,
    scrollbarMinSize: 25,
    forceVisible: false
}

export default FefferyScrollbars;