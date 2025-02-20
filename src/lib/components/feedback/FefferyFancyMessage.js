// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import toast, { Toaster } from 'react-hot-toast';
// 辅助库
import { useLoading } from '../utils';

/**
 * 美观消息提示组件FefferyFancyMessage
 */
const FefferyFancyMessage = ({
    id,
    children,
    className,
    style,
    visible = true,
    position = 'top-center',
    reverseOrder = true,
    containerClassName,
    containerStyle,
    gutter = 8,
    type = 'blank',
    duration = 4000,
    icon,
    setProps
}) => {

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
        reverseOrder={reverseOrder}
        containerClassName={containerClassName}
        containerStyle={containerStyle}
        gutter={gutter}
        data-dash-is-loading={useLoading()} />);
}

FefferyFancyMessage.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，设置内嵌元素内容
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 主动设置是否可见
     * 默认值：`false`
     */
    visible: PropTypes.bool,

    /**
     * 设置消息提示的弹出方位，可选的有`'top-left'`、`'top-center'`、`'top-right'`、`'bottom-left'`、`'bottom-center'`、`'bottom-right'`
     * 默认值：`'top-center'`
     */
    position: PropTypes.oneOf([
        'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'
    ]),

    /**
     * 设置较新的消息提示是否从底部进行追加
     * 默认值：`true`
     */
    reverseOrder: PropTypes.bool,

    /**
     * 设置容器的`css`类名
     */
    containerClassName: PropTypes.string,

    /**
     * 设置容器的`css`样式
     */
    containerStyle: PropTypes.object,

    /**
     * 设置相邻消息提示之间的像素间距
     * 默认值：`8`
     */
    gutter: PropTypes.number,

    /**
     * 设置信息类型，可选的有`'blank'`、`'success'`、`'error'`
     * 默认值：`'blank'`
     */
    type: PropTypes.oneOf(['blank', 'success', 'error']),

    /**
     * 设置消息提示显示时长（单位：毫秒）
     * 默认值：`4000`
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
};

export default FefferyFancyMessage;