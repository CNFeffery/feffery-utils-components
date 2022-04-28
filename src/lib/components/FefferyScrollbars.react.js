import { Scrollbars } from 'react-custom-scrollbars';

// 定义自定义滚动条容器组件FefferyScrollbars
const FefferyScrollbars = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
        thumbSize,
        thumbMinSize,
        autoHide,
        autoHideTimeout,
        autoHideDuration,
        loading_state
    } = props;

    return <Scrollbars
        id={id}
        style={style}
        className={className}
        thumbSize={thumbSize}
        thumbMinSize={thumbMinSize}
        autoHide={autoHide}
        autoHideTimeout={autoHideTimeout}
        autoHideDuration={autoHideDuration}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >
        {children}
    </ Scrollbars>;
}


// 定义参数或属性
FefferyScrollbars.propTypes = {
    // 部件id
    id: PropTypes.string,

    children: PropTypes.node,

    style: PropTypes.object,

    className: PropTypes.string,

    // 设置滚动条像素高度，默认为30
    thumbSize: PropTypes.number,

    // 设置当鼠标移出滚动条区域时是否隐藏滚动条，默认为false
    autoHide: PropTypes.bool,

    // 设置鼠标移出 滚动条区域多少毫秒后隐藏滚动条，默认为1000
    autoHideTimeout: PropTypes.number,

    // 设置滚动条显隐动画耗时毫秒数，默认为200
    autoHideDuration: PropTypes.number,

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
    autoHide: false,
    thumbSize: 30,
    autoHideTimeout: 1000,
    autoHideDuration: 200
}

export default FefferyScrollbars;