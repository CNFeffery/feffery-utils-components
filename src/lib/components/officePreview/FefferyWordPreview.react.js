import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyWordPreview = React.lazy(() => import(/* webpackChunkName: "feffery_word_preview" */ '../../fragments/officePreview/FefferyWordPreview.react'));

const FefferyWordPreview = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyWordPreview {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyWordPreview.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 必填，设置目标excel文件资源地址
     */
    src: PropTypes.string.isRequired,

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
FefferyWordPreview.defaultProps = {
}

export default FefferyWordPreview;

export const propTypes = FefferyWordPreview.propTypes;
export const defaultProps = FefferyWordPreview.defaultProps;