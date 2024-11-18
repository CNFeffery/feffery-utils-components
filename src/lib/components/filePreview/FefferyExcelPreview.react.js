import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyExcelPreview = React.lazy(() => import(/* webpackChunkName: "feffery_excel_preview" */ '../../fragments/filePreview/FefferyExcelPreview.react'));

/**
 * excel文件预览组件FefferyExcelPreview
 */
const FefferyExcelPreview = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyExcelPreview {...props} />
        </Suspense>
    );
}

FefferyExcelPreview.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.string,

    /**
     * 必填，设置目标`excel`文件资源地址
     */
    src: PropTypes.string.isRequired,

    /**
     * 至少渲染的列数，当设置为`0`时会自动根据数据列数进行渲染
     */
    minColLength: PropTypes.number,

    /**
     * 至少渲染的行数，当设置为`0`时会自动根据数据行数进行渲染
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