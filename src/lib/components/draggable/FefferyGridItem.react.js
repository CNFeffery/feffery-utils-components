import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGridItem = React.lazy(() => import(/* webpackChunkName: "feffery_grid" */ '../../fragments/draggable/FefferyGridItem.react'));

const FefferyGridItem = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGridItem {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyGridItem.propTypes = {
    /**
     * 部件id
     */
    id: PropTypes.string,

    /**
     * 设置要嵌套的子元素
     */
    children: PropTypes.node,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 用于为当前可拖拽网格项设置唯一的标识key值
     */
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

export default FefferyGridItem;

export const propTypes = FefferyGridItem.propTypes;
export const defaultProps = FefferyGridItem.defaultProps;