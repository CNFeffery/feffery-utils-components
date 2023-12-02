import React, { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';

// 定义跨标签页通信器FefferyTabMessenger
const FefferyTabMessenger = (props) => {
    // 取得必要属性或参数
    const {
        role,
        targetUrl,
        toSendMessage,
        targetWindowFeatures,
        setProps,
        loading_state
    } = props;

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


// 定义参数或属性
FefferyTabMessenger.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新组件状态用
     */
    key: PropTypes.string,

    /**
     * 必填，声明当前组件所在标签页角色，可选的有'sender'和'receiver'
     */
    role: PropTypes.oneOf(['sender', 'receiver']).isRequired,

    /**
     * 当role为'sender'时，用于定义自动创建打开的目标标签页对应url
     */
    targetUrl: PropTypes.string,

    /**
     * 当role为'sender'时，用于定义自动创建打开的目标标签页底层调用window.open()对应的额外的windowFeatures字符串
     */
    targetWindowFeatures: PropTypes.string,

    /**
     * 当role为'sender'时，用于设置将要新发送的信息内容，每次成功发送后都会重置为空
     */
    toSendMessage: PropTypes.string,

    /**
     * 当role为'receiver'时，用于监听最近一次收到的信息内容
     */
    recivedMessage: PropTypes.string,

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
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyTabMessenger.defaultProps = {
}

export default FefferyTabMessenger;