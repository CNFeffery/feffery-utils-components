// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useTitle } from 'ahooks';

/**
 * 页面title设置组件FefferySetTitle
 */
const FefferySetTitle = ({
    title,
    originTitle,
    setProps
}) => {

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
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

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
    setProps: PropTypes.func
};

export default FefferySetTitle;