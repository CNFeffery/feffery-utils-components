// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * 文件下载组件FefferyDownload
 */
const FefferyDownload = (props) => {
    const {
        file,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        if (file) {
            // 模拟下载指定文件
            let downloadTarget = document.createElement('a')
            downloadTarget.target = '_blank'
            downloadTarget.href = file.url
            downloadTarget.download = file.name || 'download'
            document.body.appendChild(downloadTarget)
            downloadTarget.click()
            downloadTarget.remove()
            // 重置file
            setProps({ file: null })
        }
    }, [file])

    return <></>;
}

FefferyDownload.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置新的下载任务对应文件信息，每次触发下载后都会重置为空值
     */
    file: PropTypes.exact({
        /**
         * 必填，文件资源地址
         */
        url: PropTypes.string.isRequired,
        /**
         * 自定义文件下载后的文件名，可省略后缀名
         */
        name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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
    })
};

FefferyDownload.defaultProps = {
}

export default FefferyDownload;