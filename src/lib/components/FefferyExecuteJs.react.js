import { Component } from 'react';


// 定义js直接执行部件FefferyExecuteJs
export default class FefferyExecuteJs extends Component {
    render() {
        // 取得必要属性或参数
        const {
            jsString
        } = this.props;

        // 执行原生js程序
        if (jsString) {
            eval(jsString)
        }

        return <></>
    }

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