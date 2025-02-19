// 组件核心
import { AwesomeButton } from 'react-awesome-button';
// 辅助库
import { isString } from 'lodash';
import { useRequest } from 'ahooks';
import { useLoading } from '../../components/utils';
// 自定义hooks
import useCss from '../../hooks/useCss';
// 样式
import AwesomeButtonStyles from 'react-awesome-button/src/styles/styles.scss';
// 参数类型
import { propTypes, defaultProps } from '../../components/general/FefferyFancyButton.react';

/**
 * 美观按钮组件FefferyFancyButton
 */
const FefferyFancyButton = ({
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
    setProps
}) => {

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
            data-dash-is-loading={useLoading()} >
            {children}
        </AwesomeButton>
    );
}

export default FefferyFancyButton;

FefferyFancyButton.defaultProps = defaultProps;
FefferyFancyButton.propTypes = propTypes;