import root from 'react-shadow';
import React from 'react';
import PropTypes from 'prop-types';

// 定义Shadow DOM组件FefferyShadowDom
const FefferyShadowDom = (props) => {
    // 取得必要属性或参数
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


// 定义参数或属性
FefferyShadowDom.propTypes = {
    // 部件id
    id: PropTypes.string,

    key: PropTypes.string,

    children: PropTypes.node,

    className: PropTypes.string,

    style: PropTypes.object,

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
FefferyShadowDom.defaultProps = {
}

export default FefferyShadowDom;