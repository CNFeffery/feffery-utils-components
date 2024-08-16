import { AwesomeButton } from 'react-awesome-button';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useRequest } from 'ahooks';
import AwesomeButtonStyles from 'react-awesome-button/src/styles/styles.scss';
import { propTypes, defaultProps } from '../../components/general/FefferyFancyButton.react';

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

export default FefferyFancyButton;

FefferyFancyButton.defaultProps = defaultProps;
FefferyFancyButton.propTypes = propTypes;