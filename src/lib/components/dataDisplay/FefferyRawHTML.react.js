// react核心
import PropTypes from 'prop-types';
// 组件核心
import { Interweave } from 'interweave';

/**
 * HTML字符渲染组件FefferyRawHTML
 */
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

FefferyRawHTML.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 原始`HTML`字符串
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

FefferyRawHTML.defaultProps = {
}

export default FefferyRawHTML;