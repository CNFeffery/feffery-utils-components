import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { isUndefined } from 'lodash';

// 定义sessionStorage状态管理组件
const FefferySessionStorage = (props) => {
    // 取得必要属性或参数
    const {
        id,
        data,
        setProps,
        loading_state
    } = props;

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
        if (!isUndefined(data)) {
            sessionStorage.setItem(id, JSON.stringify(data))
        }
    }, [data])

    return (
        <div
            id={id}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}


// 定义参数或属性
FefferySessionStorage.propTypes = {
    // 部件id
    id: PropTypes.string.isRequired,

    // 设置或监听当前id对应的sessionStorage数据
    data: PropTypes.any,

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
FefferySessionStorage.defaultProps = {
}

export default FefferySessionStorage;