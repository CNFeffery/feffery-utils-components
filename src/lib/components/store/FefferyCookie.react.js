// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useCookieState } from 'ahooks';

/**
 * Cookie控制组件FefferyCookie
 */
const FefferyCookie = ({
    cookieKey,
    defaultValue,
    value,
    expires,
    pathname = '/',
    secure = false,
    setProps
}) => {

    const [value_, setValue_] = useCookieState(
        cookieKey,
        {
            defaultValue: defaultValue,
            expires: expires && (() => new Date(+new Date() + expires * 1000))(),
            path: pathname,
            secure: secure
        }
    )

    useEffect(() => {
        // 初始化时，将value_值同步给value
        setProps({
            value: value_
        })
    }, [])

    useEffect(() => {
        // 每次value变化时都将最新值同步给value_
        if (value) {
            setValue_(value)
        }
    }, [value])

    return <></>;
}

FefferyCookie.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，设置要绑定的`cookie`键名
     */
    cookieKey: PropTypes.string.isRequired,

    /**
     * 为当前所绑定的`cookie`设定缺省时的默认值，当所绑定的`cookie`本身有值时，该值将不会影响原本的`cookie`值
     */
    defaultValue: PropTypes.string,

    /**
     * 用于更新当前绑定的`cookie`值
     */
    value: PropTypes.string,

    /**
     * 设置当前`cookie`值的有效存储时间，单位：秒
     */
    expires: PropTypes.number,

    /**
     * 设置当前`cookie`值可用的`pathname`
     * 默认值：`'/'`
     */
    pathname: PropTypes.string,

    /**
     * 设置当前`cookie`是否仅允许通过`https`安全传输
     * 默认值：`false`
     */
    secure: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyCookie;