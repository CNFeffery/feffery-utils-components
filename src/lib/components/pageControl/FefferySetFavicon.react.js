// react核心
import PropTypes from 'prop-types';
// 组件核心
import { useFavicon } from 'ahooks';

/**
 * favicon设置组件FefferySetFavicon
 */
const FefferySetFavicon = ({
    favicon,
    setProps
}) => {

    useFavicon(favicon);

    return <></>;
}

FefferySetFavicon.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 用于设置要更新的`favicon`图片文件地址，支持`svg`、`png`、`ico`、`gif`格式
     */
    favicon: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferySetFavicon;