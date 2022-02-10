import React, { Component } from 'react';
import PropTypes from 'prop-types';

const parseChildrenToArray = children => {
    if (children && !Array.isArray(children)) {
        return [children];
    }
    return children;
};

// 定义分割子面板组件FefferySplitPane
export default class FefferySplitPane extends Component {
    render() {
        // 取得必要属性或参数
        let {
            id,
            children,
            className,
            style,
            loading_state
        } = this.props;

        children = parseChildrenToArray(children)

        return (
            <div id={id}
                className={className}
                style={style}
                children={children}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }>
            </div>
        );
    }
}

// 定义参数或属性
FefferySplitPane.propTypes = {
    // 组件id
    id: PropTypes.string,

    children: PropTypes.node,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
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
    setProps: PropTypes.func
};

// 设置默认参数
FefferySplitPane.defaultProps = {
}