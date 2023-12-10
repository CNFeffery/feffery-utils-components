import { useEffect } from 'react';
import { useRequest } from 'ahooks';
import PropTypes from 'prop-types';

// 定义防抖属性组件FefferyDebounceProp
const FefferyDebounceProp = (props) => {
    // 取得必要属性或参数
    const {
        sourceProp,
        debounceWait,
        setProps,
        loading_state
    } = props;

    const { run: syncProp } = useRequest(
        (e) => {
            setProps({
                debounceProp: e
            })
        },
        {
            debounceWait: debounceWait,
            manual: true
        }
    )

    useEffect(() => {
        syncProp(sourceProp)
    }, [sourceProp])

    return <></>;
}

// 定义参数或属性
FefferyDebounceProp.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 用于同步目标属性，请通过回调函数更新
     */
    sourceProp: PropTypes.any,

    /**
     * 对应sourceProp的防抖控制状态
     */
    debounceProp: PropTypes.any,

    /**
     * 设置防抖延时时长，单位：毫秒
     * 默认：200
     */
    debounceWait: PropTypes.number,

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
FefferyDebounceProp.defaultProps = {
    debounceWait: 200
}

export default FefferyDebounceProp;