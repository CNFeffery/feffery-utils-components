// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useDocumentVisibility } from 'ahooks';

/**
 * 页面可见性检查组件FefferyDocumentVisibility
 */
const FefferyDocumentVisibility = ({
    setProps
}) => {

    const _documentVisibility = useDocumentVisibility();

    useEffect(() => {
        setProps({ documentVisibility: _documentVisibility })
    }, [_documentVisibility]);

    return <></>;
}

FefferyDocumentVisibility.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听页面是否可见，可选项有`'visible'`、`'hidden'`
     */
    documentVisibility: PropTypes.oneOf(['visible', 'hidden']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyDocumentVisibility;