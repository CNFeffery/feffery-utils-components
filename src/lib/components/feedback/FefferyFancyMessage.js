import { useEffect } from 'react';
import toast, { Toaster } from 'react-hot-toast';
import PropTypes from 'prop-types';

// 定义美观消息提示组件FefferyFancyMessage
const FefferyFancyMessage = (props) => {

    const {
        id,
        children,
        key,
        className,
        style,
        visible,
        position,
        reverseOrder,
        containerClassName,
        containerStyle,
        gutter,
        type,
        duration,
        icon,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        if (visible) {
            if (type === 'blank' || !type) {
                toast(
                    children,
                    {
                        duration: duration,
                        icon: icon,
                        className: className,
                        style: style,
                        position: position
                    }
                )
            } else if (type === 'success') {
                toast.success(
                    children,
                    {
                        duration: duration,
                        icon: icon,
                        className: className,
                        style: style,
                        position: position
                    }
                )
            } else if (type === 'error') {
                toast.error(
                    children,
                    {
                        duration: duration,
                        icon: icon,
                        className: className,
                        style: style,
                        position: position
                    }
                )
            }
            setProps({
                visible: false
            })
        }
    }, [visible])

    return (<Toaster
        id={id}
        key={key}
        reverseOrder={reverseOrder}
        containerClassName={containerClassName}
        containerStyle={containerStyle}
        gutter={gutter}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />);
}

// 定义参数或属性
FefferyFancyMessage.propTypes = {

    /**
     * 组件子元素
     */
    children: PropTypes.node,

    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 设置容器的css类名
     */
    className: PropTypes.string,

    /**
     * 设置容器的css样式
     */
    style: PropTypes.object,

    /**
     * 主动设置是否可见，默认为false
     */
    visible: PropTypes.bool,

    /**
     * 设置消息提示的弹出方位，可选的有'top-left'、'top-center'、'top-right'、'bottom-left'、'bottom-center'、'bottom-right'，默认为'top-center'
     */
    position: PropTypes.oneOf([
        'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'
    ]),

    /**
     * 设置较新的消息提示是否从底部进行追加，默认为true
     */
    reverseOrder: PropTypes.bool,

    /**
     * 设置容器的css类名
     */
    containerClassName: PropTypes.string,

    /**
     * 设置容器的css样式
     */
    containerStyle: PropTypes.object,

    /**
     * 设置相邻消息提示之间的像素间距，默认为8
     */
    gutter: PropTypes.number,

    /**
     * 设置信息类型，可选的有'blank', 'success', 'error'
     * 默认为'blank'
     */
    type: PropTypes.oneOf(['blank', 'success', 'error']),

    /**
     * 设置消息提示显示时长（单位：毫秒），默认为4000
     */
    duration: PropTypes.number,

    /**
     * 自定义消息提示图标
     */
    icon: PropTypes.node,

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
FefferyFancyMessage.defaultProps = {
    visible: true,
    position: 'top-center',
    reverseOrder: true,
    gutter: 8,
    duration: 4000,
    type: 'blank'
}

export default FefferyFancyMessage;