// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { ToastContainer, toast } from 'react-toastify';
// 辅助库
import { useLoading } from '../utils';
// 样式
import 'react-toastify/dist/ReactToastify.css';

/**
 * 美观通知提示组件FefferyFancyNotification
 */
const FefferyFancyNotification = ({
    id,
    children,
    className,
    style,
    type,
    visible = true,
    position,
    autoClose,
    closable = true,
    hideProgressBar,
    pauseOnHover,
    closeOnClick,
    newestOnTop,
    toastClassName,
    bodyClassName,
    progressClassName,
    progressStyle,
    draggable,
    draggablePercent,
    containerId,
    limit,
    theme,
    setProps
}) => {

    useEffect(() => {
        if (visible) {
            if (type) {
                toast(
                    children,
                    {
                        type: type,
                        containerId: containerId
                    }
                )
            } else {
                toast(
                    children,
                    {
                        containerId: containerId
                    }
                )
            }
            setProps({
                visible: false
            })
        }

    }, [visible])

    return (
        <ToastContainer
            id={id}
            className={className}
            style={style}
            position={position}
            autoClose={autoClose}
            closeButton={closable}
            hideProgressBar={hideProgressBar}
            pauseOnHover={pauseOnHover}
            closeOnClick={closeOnClick}
            newestOnTop={newestOnTop}
            toastClassName={toastClassName}
            bodyClassName={bodyClassName}
            progressClassName={progressClassName}
            progressStyle={progressStyle}
            draggable={draggable}
            draggablePercent={draggablePercent}
            containerId={containerId}
            enableMultiContainer={true}
            limit={limit}
            theme={theme}
            data-dash-is-loading={useLoading()} />
    );
}

FefferyFancyNotification.propTypes = {
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
     * 设置信息类型，可选的有`'info'`、`'success'`、`'warning'`、`'error'`
     */
    type: PropTypes.oneOf(['info', 'success', 'warning', 'error']),

    /**
     * 主动设置是否可见
     * 默认值：`false`
     */
    visible: PropTypes.bool,

    /**
     * 设置通知提示弹出方位，可选的有`'top-right'`、`'top-center'`、`'top-left'`、`'bottom-right'`、`'bottom-cente'`、`'bottom-left'`
     * 默认值：`'top-right'`
     */
    position: PropTypes.oneOf([
        'top-right', 'top-center', 'top-left', 'bottom-right', 'bottom-cente', 'bottom-left'
    ]),

    /**
     * 配置自动关闭延时（单位：毫秒），当设置为`false`时不会自动关闭
     * 默认值：`5000`
     */
    autoClose: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.number
    ]),

    /**
     * 设置是否可关闭
     * 默认值：`true`
     */
    closable: PropTypes.bool,

    /**
     * 设置是否显示关闭倒计时进度条
     * 默认值：`false`
     */
    hideProgressBar: PropTypes.bool,

    /**
     * 设置当鼠标悬浮于通知框上时，是否暂停倒计时
     * 默认值：`true`
     */
    pauseOnHover: PropTypes.bool,

    /**
     * 设置是否允许通知框在被点击后自动关闭
     * 默认值：`true`
     */
    closeOnClick: PropTypes.bool,

    /**
     * 设置是否将新的通知框显示在更顶端的位置
     * 默认值：`false`
     */
    newestOnTop: PropTypes.bool,

    /**
     * 设置通知框的`css`类
     */
    toastClassName: PropTypes.string,

    /**
     * 设置通知框内容区的`css`类
     */
    bodyClassName: PropTypes.string,

    /**
     * 设置通知框进度条的`css`类
     */
    progressClassName: PropTypes.string,

    /**
     * 设置通知框进度条的`css`样式
     */
    progressStyle: PropTypes.object,

    /**
     * 设置通知框是否可拖拽
     * 默认值：`true`
     */
    draggable: PropTypes.bool,

    /**
     * 设置通知框被拖拽距离占自身宽度的百分比阈值，拖拽距离超出此阈值时通知框会被关闭
     * 默认值：`80`
     */
    draggablePercent: PropTypes.number,

    /**
     * 可选，设置局部目标容器的`id`
     */
    containerId: PropTypes.string,

    /**
     * 设置屏幕中允许同时显示的通知框数量上限，默认无上限
     */
    limit: PropTypes.number,

    /**
     * 设置主题，可选的有`'light'`、`'dark'`、`'colored'`
     * 默认值：`'light'`
     */
    theme: PropTypes.oneOf([
        'light', 'dark', 'colored'
    ]),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyFancyNotification;