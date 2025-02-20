// react核心
import React, { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';

/**
 * 跨标签页通信组件FefferyTabMessenger
 */
const FefferyTabMessenger = ({
    role,
    targetUrl,
    toSendMessage,
    targetWindowFeatures,
    setProps
}) => {

    const targetWindowRef = useRef(null);

    useEffect(() => {
        // 若当前组件角色为收信者
        if (role === 'receiver') {
            const destorySelf = () => {
                window.close();
            }

            const listenMessage = (e) => {
                if (e.source === window.opener) {
                    setProps({
                        recivedMessage: e.data
                    });
                }
            }

            window.opener.addEventListener(
                "beforeunload",
                destorySelf
            )

            window.addEventListener(
                "message",
                listenMessage
            );

            return () => {
                window.opener.removeEventListener("beforeunload", destorySelf);
                window.removeEventListener("message", listenMessage);
            };
        } else if (role === 'sender') {
            let targetWindow = window.open(targetUrl, '_blank', targetWindowFeatures)
            targetWindowRef.current = targetWindow;
            // 当前组件销毁后，关闭目标窗口
            return () => {
                targetWindowRef.current.close();
            };
        }
    }, []);

    useEffect(() => {
        if (role === 'sender' && toSendMessage) {
            targetWindowRef.current.postMessage(toSendMessage, '*');
            setProps({
                toSendMessage: null
            })
        }
    }, [toSendMessage]);

    return <></>;
}

FefferyTabMessenger.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，声明当前组件所在标签页角色，可选的有`'sender'`和`'receiver'`
     */
    role: PropTypes.oneOf(['sender', 'receiver']).isRequired,

    /**
     * 当`role='sender'`时，用于定义自动创建打开的目标标签页对应`url`
     */
    targetUrl: PropTypes.string,

    /**
     * 当`role='sender'`时，用于定义自动创建打开的目标标签页底层调用`window.open()`对应的额外的windowFeatures字符串
     */
    targetWindowFeatures: PropTypes.string,

    /**
     * 当`role='sender'`时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空
     */
    toSendMessage: PropTypes.any,

    /**
     * 当`role='receiver'`时，用于监听最近一次收到的信息内容
     */
    recivedMessage: PropTypes.any,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyTabMessenger;