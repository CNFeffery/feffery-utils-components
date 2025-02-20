// react核心
import { useEffect } from "react";
// 组件核心
import autofit from "autofit.js";
// 参数类型
import { propTypes, defaultProps } from '../../components/resizable/FefferyAutoFit.react';

/**
 * 自适应组件FefferyAutoFit
 */
const FefferyAutoFit = ({
    id,
    containerId,
    dw,
    dh,
    resize,
    ignore,
    transition,
    delay,
    limit,
    close,
    setProps
}) => {

    useEffect(() => {
        autofit.init({
            el: containerId == 'body' ? containerId : `#${containerId}`,
            dw: dw,
            dh: dh,
            resize: resize,
            ignore: ignore,
            transition: transition,
            delay: delay,
            limit: limit
        });
    }, []);

    useEffect(() => {
        if (close) {
            autofit.off(containerId);
            setProps({ close: false });
        }
    }, [close]);

    return (
        <></>
    );
}

export default FefferyAutoFit;

FefferyAutoFit.defaultProps = defaultProps;
FefferyAutoFit.propTypes = propTypes;