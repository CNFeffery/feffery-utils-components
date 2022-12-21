import { AwesomeButton } from 'react-awesome-button';
import useCss from '../hooks/useCss';
import { isString } from 'lodash';
import { useRequest } from 'ahooks';
import AwesomeButtonStyles from 'react-awesome-button/src/styles/styles.scss';
import PropTypes from 'prop-types';

// 定义美观按钮组件FefferyFancyButton
const FefferyFancyButton = (props) => {
    // 取得必要属性或参数
    let {
        id,
        children,
        className,
        style,
        key,
        nClicks,
        debounceWait,
        type,
        disabled,
        href,
        target,
        before,
        after,
        ripple,
        setProps,
        loading_state
    } = props;

    const { run: onClick } = useRequest(
        () => {
            nClicks++;
            // 更新nClicks
            setProps({ nClicks: nClicks })
        },
        {
            debounceWait: debounceWait,
            debounceLeading: true,
            manual: true
        }
    )

    return (
        <AwesomeButton
            id={id}
            children={children}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            key={key}
            type={type}
            disabled={disabled}
            href={href}
            target={target}
            before={before}
            after={after}
            onPress={onClick}
            cssModule={AwesomeButtonStyles}
            ripple={ripple}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >{children}</AwesomeButton>
    );
}


// 定义参数或属性
FefferyFancyButton.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置按钮内嵌元素内容
    children: PropTypes.node,

    // css类名
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    // 自定义css字典
    style: PropTypes.object,

    // 辅助刷新用唯一标识key值
    key: PropTypes.string,

    // 记录按钮从渲染后开始被点击的次数，默认为0
    nClicks: PropTypes.number,

    // 用于配置value变化更新的防抖等待时长（单位：毫秒），默认为0
    debounceWait: PropTypes.number,

    // 设置按钮类型，可选的有'primary'、'secondary'、'danger'
    // 默认为'primary'
    type: PropTypes.oneOf(['primary', 'secondary', 'danger']),

    // 设置是否禁用当前按钮，默认为false
    disabled: PropTypes.bool,

    // 当按钮充当链接功能时，用于设置链接地址
    href: PropTypes.string,

    // 设置按钮的target属性，默认为'_blank'
    target: PropTypes.string,

    // 设置按钮前缀图标元素
    before: PropTypes.node,

    // 设置按钮后缀图标元素
    after: PropTypes.node,

    // 设置是否开启点击涟漪效果，默认为false
    ripple: PropTypes.bool,

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
FefferyFancyButton.defaultProps = {
    nClicks: 0,
    debounceWait: 0,
    target: '_blank'
}

export default FefferyFancyButton;