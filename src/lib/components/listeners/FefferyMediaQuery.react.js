// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useMediaQuery } from '@reactuses/core';

/**
 * 媒体查询监听组件FefferyMediaQuery
 */
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

FefferyMediaQuery.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，定义媒体查询条件
     */
    query: PropTypes.string.isRequired,

    /**
     * 监听当前媒体查询是否满足
     */
    isMatch: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyMediaQuery;