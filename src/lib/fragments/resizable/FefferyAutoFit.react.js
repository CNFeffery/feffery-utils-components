import { useEffect } from "react";
import autofit from "autofit.js";
import { propTypes, defaultProps } from '../../components/resizable/FefferyAutoFit.react';

/**
 * 自适应组件FefferyAutoFit
 */
const FefferyAutoFit = (props) => {
    // 取得必要属性或参数
    const {
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
        setProps,
        loading_state
    } = props;

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