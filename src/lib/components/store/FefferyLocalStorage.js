import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { isUndefined } from 'lodash';

// 定义localStorage状态管理组件
const FefferyLocalStorage = (props) => {
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
                const existsData = localStorage.getItem(id);
                if (existsData) {
                    setProps({
                        data: JSON.parse(existsData)
                    });
                }
            }
        }

        window.addEventListener(
            "localStorageSetItem",
            syncStorage
        );

        return () => {
            window.removeEventListener("localStorageSetItem", syncStorage);
        };
    }, []);

    useEffect(() => {
        const existsData = localStorage.getItem(id);
        if (existsData) {
            setProps({
                data: JSON.parse(existsData)
            });
        }
    }, [])

    useEffect(() => {
        if (!isUndefined(data)) {
            localStorage.setItem(id, JSON.stringify(data))
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
FefferyLocalStorage.propTypes = {
    // 部件id
    id: PropTypes.string.isRequired,

    // 设置或监听当前id对应的localStorage数据
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
FefferyLocalStorage.defaultProps = {
}

export default FefferyLocalStorage;