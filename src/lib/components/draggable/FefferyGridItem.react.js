import React from 'react';
import PropTypes from 'prop-types';

// 定义可拖拽网格项组件FefferyGridItem
const FefferyGridItem = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
        key,
        setProps,
        loading_state
    } = props;

    return (
        <div
            id={id}
            key={key}
            style={style}
            className={className}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >{children}</div>
    );
}

// 定义参数或属性
FefferyGridItem.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置要嵌套的子元素
    children: PropTypes.node,

    style: PropTypes.object,

    className: PropTypes.string,

    // 用于为当前可拖拽网格项设置唯一的标识key值
    key: PropTypes.string,

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
FefferyGridItem.defaultProps = {
}

export default React.memo(FefferyGridItem);