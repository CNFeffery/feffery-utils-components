import { Interweave } from 'interweave';
import PropTypes from 'prop-types';

// 定义原始HTML字符渲染组件FefferyRawHTML
const FefferyRawHTML = (props) => {

    const {
        id,
        key,
        htmlString,
        setProps,
        loading_state
    } = props;

    return (<Interweave
        id={id}
        key={key}
        content={htmlString}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />);
}

// 定义参数或属性
FefferyRawHTML.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 要渲染的原始HTML内容字符串
     */
    htmlString: PropTypes.string,

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
FefferyRawHTML.defaultProps = {
}

export default FefferyRawHTML;