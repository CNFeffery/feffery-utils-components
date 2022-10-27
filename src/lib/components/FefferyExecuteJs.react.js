import { useEffect } from 'react';
import PropTypes from 'prop-types';

// 定义js直接执行部件FefferyExecuteJs
const FefferyExecuteJs = (props) => {
    // 取得必要属性或参数
    const {
        id,
        jsString,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        // 执行原生js程序
        if (jsString) {
            try { eval(jsString) }
            catch (exception) { console.log(exception) }
            // 清空jsString
            setProps({
                jsString: ''
            })
        }
    }, [jsString])

    return (
        <div
            id={id}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}


// 定义参数或属性
FefferyExecuteJs.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置要执行的js代码字符串
    jsString: PropTypes.string,

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
FefferyExecuteJs.defaultProps = {
}

export default FefferyExecuteJs;