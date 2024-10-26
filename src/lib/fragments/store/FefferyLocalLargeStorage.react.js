import React, { useEffect } from 'react';
import { propTypes, defaultProps } from '../../components/store/FefferyLocalLargeStorage.react';
import localforage from 'localforage';
import { isUndefined } from 'lodash';

/**
 * 客户端大容量存储器FefferyLocalLargeStorage
 */
const FefferyLocalLargeStorage = (props) => {
    // 取得必要属性或参数
    const {
        id,
        data,
        initialSync,
        setProps,
        loading_state
    } = props;

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