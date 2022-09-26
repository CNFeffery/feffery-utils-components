import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

// 定义排序项组件FefferySortableItem
const FefferySortableItem = (props) => {
    const {
        id,
        children,
        style,
        className,
        setProps,
        loading_state
    } = props;

    return (<div
        id={id}
        style={style}
        className={className}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >{children}</div>);
}

// 定义参数或属性
FefferySortableItem.propTypes = {

    children: PropTypes.node,

    id: PropTypes.string,

    style: PropTypes.object,

    className: PropTypes.string,

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
FefferySortableItem.defaultProps = {
}

export default React.memo(FefferySortableItem);