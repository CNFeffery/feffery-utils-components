// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 辅助库
import { isUndefined } from 'lodash';

/**
 * sessionStorage状态管理组件
 */
const FefferySessionStorage = ({
    id,
    data,
    initialSync = false,
    setProps
}) => {

    useEffect(() => {
        const syncStorage = (e) => {
            if (e.triggerKey === id) {
                const existsData = sessionStorage.getItem(id);
                if (existsData) {
                    setProps({
                        data: JSON.parse(existsData)
                    });
                }
            }
        }

        window.addEventListener(
            "sessionStorageSetItem",
            syncStorage
        );

        return () => {
            window.removeEventListener("sessionStorageSetItem", syncStorage);
        };
    }, []);

    useEffect(() => {
        if (initialSync) {
            const existsData = sessionStorage.getItem(id);
            if (existsData) {
                setProps({
                    data: JSON.parse(existsData)
                });
            }
        }
    }, [])

    useEffect(() => {
        if (!isUndefined(data)) {
            sessionStorage.setItem(id, JSON.stringify(data))
        }
    }, [data])

    return <></>;
}

FefferySessionStorage.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string.isRequired,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置或监听当前`id`对应的`sessionStorage`数据
     */
    data: PropTypes.any,

    /**
     * 设置初始化时是否从`sessionStorage`中尝试读取`id`对应的值并更新到`data`中
     * 默认值：`false`
     */
    initialSync: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferySessionStorage;