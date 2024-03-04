import { useEffect } from 'react';
import { useMediaQuery } from '@reactuses/core';
import PropTypes from 'prop-types';

// 定义媒体查询监听组件FefferyMediaQuery
const FefferyMediaQuery = (props) => {
    const {
        query,
        setProps
    } = props;

    const _isMatch = useMediaQuery(query);

    useEffect(() => {
        setProps({ isMatch: _isMatch })
    }, [_isMatch]);

    return <></>;
}

// 定义参数或属性
FefferyMediaQuery.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * 必填，定义媒体查询条件
     */
    query: PropTypes.string.isRequired,

    /**
     * 是否满足当前媒体查询
     */
    isMatch: PropTypes.bool,

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
FefferyMediaQuery.defaultProps = {
}

export default FefferyMediaQuery;