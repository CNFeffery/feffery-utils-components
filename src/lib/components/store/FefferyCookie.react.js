import { useEffect } from 'react';
import { useCookieState } from 'ahooks';
import PropTypes from 'prop-types';

// 定义cookie控制组件FefferyCookie
const FefferyCookie = (props) => {
    // 取得必要属性或参数
    const {
        id,
        cookieKey,
        defaultValue,
        value,
        expires,
        pathname,
        secure,
        setProps,
        loading_state
    } = props;

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

// 定义参数或属性
FefferyCookie.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置要绑定的cookie键名，必填
    cookieKey: PropTypes.string.isRequired,

    // 为当前所绑定的cookie设定缺省时的默认值
    // 当所绑定的cookie本身有值时，该值将不会影响原本的cookie值
    defaultValue: PropTypes.string,

    // 用于更新当前绑定的cookie值
    value: PropTypes.string,

    // 设置当前cookie值的有效存储时间，单位：秒
    expires: PropTypes.number,

    // 设置当前cookie值可用的pathname，默认为'/'
    pathname: PropTypes.string,

    // 设置当前cookie是否仅允许通过https安全传输，默认为false
    secure: PropTypes.bool,

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
FefferyCookie.defaultProps = {
    pathname: '/',
    secure: false
}

export default FefferyCookie;