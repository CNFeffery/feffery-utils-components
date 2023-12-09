import { useTitle } from 'ahooks';
import PropTypes from 'prop-types';

// 定义页面title设置组件FefferySetTitle
const FefferySetTitle = (props) => {

    const {
        id,
        title,
        setProps,
        loading_state
    } = props;

    // 随着title更新进而改变页面title
    if (title) {
        useTitle(title)
    }

    return <></>;
}

// 定义参数或属性
FefferySetTitle.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 用于设置要更新的title信息
     */
    title: PropTypes.string,

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
FefferySetTitle.defaultProps = {
}

export default FefferySetTitle;