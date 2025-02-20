import { useEffect } from 'react';
import axios from 'axios';
import { propTypes, defaultProps } from '../../components/communication/FefferyHttpRequests.react';

/**
 * http请求组件FefferyHttpRequests
 */
const FefferyHttpRequests = ({
    requestConfig,
    status,
    setProps
}) => {

    // 处理新的请求任务
    useEffect(() => {
        if (requestConfig) {
            // 更新状态为pending
            setProps({ status: 'pending' })
            fetchData(requestConfig)
        }
        // 重置requestConfig
        setProps({ requestConfig: null })
    }, [requestConfig])

    const fetchData = async (newConfig) => {
        axios(newConfig)
            .then(res => {
                setProps({
                    responseResult: {
                        status: res.status,
                        statusText: res.statusText,
                        data: res.data,
                        requestURL: res.request.responseURL,
                        timestamp: new Date().getTime()
                    },
                    // 更新状态为idle
                    status: 'idle'
                })
            })
            .catch(err => {
                setProps({
                    responseResult: {
                        status: err.response?.status,
                        statusText: err.response?.statusText,
                        data: err.response?.data,
                        requestURL: err.request.responseURL,
                        timestamp: new Date().getTime(),
                        code: err.code,
                        message: err.message,
                    },
                    // 更新状态为idle
                    status: 'idle'
                })
            })
    }

    return <></>;
}

export default FefferyHttpRequests;

FefferyHttpRequests.defaultProps = defaultProps;
FefferyHttpRequests.propTypes = propTypes;