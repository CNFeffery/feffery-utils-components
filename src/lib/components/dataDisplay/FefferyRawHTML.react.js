// react核心
import PropTypes from 'prop-types';
// 组件核心
import { Interweave } from 'interweave';
// 辅助库
import { useLoading } from '../utils';

/**
 * HTML字符渲染组件FefferyRawHTML
 */
const FefferyRawHTML = ({
    id,
    key,
    htmlString,
    setProps
}) => {

    return (<Interweave
        id={id}
        key={key}
        content={htmlString}
        data-dash-is-loading={useLoading()} />);
}

FefferyRawHTML.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 原始`HTML`字符串
     */
    htmlString: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyRawHTML;