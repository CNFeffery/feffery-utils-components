import { useEffect } from 'react';


// 定义js直接执行部件FefferyExecuteJs
const FefferyExecuteJs = (props) => {
    // 取得必要属性或参数
    const {
        id,
        jsString,
        loading_state
    } = props;

    useEffect(() => {
        // 执行原生js程序
        if (jsString) {
            eval(jsString)
        }
    }, [jsString])

    return <div
        id={id}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />;
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
    })
};

// 设置默认参数
FefferyExecuteJs.defaultProps = {
}

export default FefferyExecuteJs;