import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyExcelPreview = React.lazy(() => import(/* webpackChunkName: "feffery_excel_preview" */ '../../fragments/filePreview/FefferyExcelPreview.react'));

const FefferyExcelPreview = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyExcelPreview {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyExcelPreview.propTypes = {
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

    /**
     * 至少渲染的列数，当设置为0时会自动根据数据列数进行渲染
     */
    minColLength: PropTypes.number,

    /**
     * 至少渲染的行数，当设置为0时会自动根据数据行数进行渲染
     */
    minRowLength: PropTypes.number,

    /**
     * 默认列宽的基础上额外增加的像素列宽
     */
    widthOffset: PropTypes.number,

    /**
     * 默认行高的基础上额外增加的像素行高
     */
    heightOffset: PropTypes.number,

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
FefferyExcelPreview.defaultProps = {
}

export default FefferyExcelPreview;

export const propTypes = FefferyExcelPreview.propTypes;
export const defaultProps = FefferyExcelPreview.defaultProps;