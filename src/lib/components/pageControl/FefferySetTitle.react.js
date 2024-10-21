import { useEffect } from 'react';
import { useTitle } from 'ahooks';
import PropTypes from 'prop-types';

/**
 * 页面title设置组件FefferySetTitle
 */
const FefferySetTitle = (props) => {

    const {
        title,
        originTitle,
        setProps,
        loading_state
    } = props;

    // 组件卸载时，还原有效的originTitle
    useEffect(() => {
        return () => {
            if (originTitle) {
                document.title = originTitle;
            }
        }
    }, [])

    // 处理title变化时的更新
    useTitle(title || originTitle);

    return <></>;
}

FefferySetTitle.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 用于设置要更新的`title`信息
     */
    title: PropTypes.string,

    /**
     * 当`title`参数为空，或当前组件从页面中卸载后应当还原的`title`
     */
    originTitle: PropTypes.string,

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