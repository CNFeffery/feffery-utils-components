import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGridItem = React.lazy(() => import(/* webpackChunkName: "feffery_grid" */ '../../fragments/draggable/FefferyGridItem.react'));

/**
 * 可拖拽网格项组件FefferyGridItem
 */
const FefferyGridItem = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGridItem {...props} />
        </Suspense>
    );
}

FefferyGridItem.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 用于为当前可拖拽网格项设置唯一标识`key`值
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

FefferyGridItem.defaultProps = {
}

export default FefferyGridItem;

export const propTypes = FefferyGridItem.propTypes;
export const defaultProps = FefferyGridItem.defaultProps;