import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyBarcode = React.lazy(() => import(/* webpackChunkName: "feffery_barcode" */ '../../fragments/dataDisplay/FefferyBarcode.react'));

/**
 * 条形码组件FefferyBarcode
 */
const FefferyBarcode = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyBarcode {...props} />
        </Suspense>
    );
}

FefferyBarcode.propTypes = {
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
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 渲染类型，可选的有`'img'`、`'svg'`、`'canvas'`
     * 默认值：`'canvas'`
     */
    renderer: PropTypes.oneOf(['img', 'svg', 'canvas']),

    /**
     * 设置条形码所表达的信息值
     */
    value: PropTypes.string,

    /**
     * 设置要使用的条形码类型，可选的有`'CODE128'`、`'CODE128A'`、`'CODE128B'`、`'CODE128C'`、`'EAN2'`、`'EAN5'`、`'EAN8'`、`'EAN13'`、`'UPC'`、`'CODE39'`、`'ITF14'`、`'MSI'`、`'MSI10'`、`'MSI11'`、`'MSI1010'`、`'MSI1110'`、`'pharmacode'`、`'codabar'`
     * 默认值：`'CODE128'`
     */
    format: PropTypes.oneOf(['CODE128', 'CODE128A', 'CODE128B', 'CODE128C', 'EAN2', 'EAN5', 'EAN8', 'EAN13', 'UPC', 'CODE39', 'ITF14', 'MSI', 'MSI10', 'MSI11', 'MSI1010', 'MSI1110', 'pharmacode', 'codabar']),

    /**
     * 设置条形码宽度
     * 默认值：`2`
     */
    width: PropTypes.number,

    /**
     * 设置条形码高度
     * 默认值：`100`
     */
    height: PropTypes.number,

    /**
     * 设置是否显示条形码所表达的信息值
     * 默认值：`true`
     */
    displayValue: PropTypes.bool,

    /**
     * 设置条形码显示的文本
     */
    text: PropTypes.string,

    /**
     * 设置条形码显示文本的字体样式
     * 默认值：''
     */
    fontOptions: PropTypes.string,

    /**
     * 设置条形码显示文本的字体种类
     * 默认值：'monospace'
     */
    font: PropTypes.string,

    /**
     * 设置条形码显示文本的字体大小
     * 默认值：`20`
     */
    fontSize: PropTypes.number,

    /**
     * 设置条形码显示文本的水平对齐方式，可选的有`'left'`、`'center'`、`'right'`
     * 默认值：`'center'`
     */
    textAlign: PropTypes.oneOf(['left', 'center', 'right']),

    /**
     * 设置条形码显示文本的垂直位置，可选的有`'top'`、`'bottom'`
     * 默认值：`'bottom'`
     */
    textPosition: PropTypes.oneOf(['top', 'bottom']),

    /**
     * 设置条形码和显示文本之间的间距
     * 默认值：`2`
     */
    textMargin: PropTypes.number,

    /**
     * 设置条形码的背景颜色
     * 默认值：`'#ffffff'`
     */
    background: PropTypes.string,

    /**
     * 设置条形码的线条和显示文本颜色
     * 默认值：`'#000000'`
     */
    lineColor: PropTypes.string,

    /**
     * 设置条形码周围的间距边距，如果未设置`marginTop`、`marginBottom`、`marginLeft`、`marginRight`，则这四个参数将继承`margins`的值
     * 默认值：`10`
     */
    margin: PropTypes.number,

    /**
     * 设置条形码周围的上间距边距
     */
    marginTop: PropTypes.number,

    /**
     * 设置条形码周围的下间距边距
     */
    marginBottom: PropTypes.number,

    /**
     * 设置条形码周围的左间距边距
     */
    marginLeft: PropTypes.number,

    /**
     * 设置条形码周围的右间距边距
     */
    marginRight: PropTypes.number,

    /**
     * 设置条形码是否保持平整，仅适用于`EAN8`和`EAN13`
     * 默认值：`false`
     */
    flat: PropTypes.bool,

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
FefferyBarcode.defaultProps = {
    renderer: 'canvas',
    format: 'CODE128',
    width: 2,
    height: 100,
    displayValue: true,
    fontOptions: '',
    font: 'monospace',
    fontSize: 20,
    textAlign: 'center',
    textPosition: 'bottom',
    textMargin: 2,
    background: '#ffffff',
    lineColor: '#000000',
    margin: 10,
    flat: false
}

export default FefferyBarcode;

export const propTypes = FefferyBarcode.propTypes;
export const defaultProps = FefferyBarcode.defaultProps;