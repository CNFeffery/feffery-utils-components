// react核心
import React, { useEffect } from 'react';
// 组件核心
import localforage from 'localforage';
// 辅助库
import { isUndefined } from 'lodash';
// 参数类型
import { propTypes, defaultProps } from '../../components/store/FefferyLocalLargeStorage.react';

/**
 * 客户端大容量存储器FefferyLocalLargeStorage
 */
const FefferyLocalLargeStorage = ({
    id,
    data,
    initialSync,
    setProps
}) => {

    useEffect(() => {
        (async () => {
            if (initialSync) {
                try {
                    const existsData = await localforage.getItem(id);
                    if (existsData) {
                        setProps({
                            data: JSON.parse(existsData)
                        });
                    }
                } catch (err) {
                    console.error(err);
                }
            }
        })()
    }, [])

    useEffect(() => {
        (async () => {
            if (!isUndefined(data)) {
                try {
                    await localforage.setItem(id, JSON.stringify(data))
                } catch (err) {
                    console.error(err);
                }
            }
        })()
    }, [data])

    return <></>;
}

export default React.memo(FefferyLocalLargeStorage);

FefferyLocalLargeStorage.defaultProps = defaultProps;
FefferyLocalLargeStorage.propTypes = propTypes;