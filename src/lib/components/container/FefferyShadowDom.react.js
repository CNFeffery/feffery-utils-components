// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import root from 'react-shadow';

/**
 * Shadow DOM组件FefferyShadowDom
 */
const FefferyShadowDom = (props) => {
    const {
        id,
        key,
        children,
        className,
        style,
        setProps,
        loading_state
    } = props;

    return (
        <root.div
            id={id}
            key={key}
            className={className}
            style={style}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >
            {children}
        </ root.div>
    );
}

FefferyShadowDom.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，内嵌元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

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

FefferyShadowDom.defaultProps = {
}

export default FefferyShadowDom;