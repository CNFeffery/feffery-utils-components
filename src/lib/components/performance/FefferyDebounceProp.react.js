// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useRequest } from 'ahooks';

/**
 * 防抖属性组件FefferyDebounceProp
 */
const FefferyDebounceProp = ({
    sourceProp,
    debounceWait = 200,
    setProps
}) => {

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

FefferyDebounceProp.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 用于同步目标属性，请通过回调函数更新
     */
    sourceProp: PropTypes.any,

    /**
     * 对应`sourceProp`的防抖控制状态
     */
    debounceProp: PropTypes.any,

    /**
     * 设置防抖延时时长，单位：毫秒
     * 默认值：`200`
     */
    debounceWait: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyDebounceProp;