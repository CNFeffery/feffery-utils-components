import jsPreviewDocx from "@js-preview/docx";
import { useRef, useEffect } from 'react';
import '@js-preview/docx/lib/index.css';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/filePreview/FefferyWordPreview.react';

// 定义word文件预览组件FefferyWordPreview
const FefferyWordPreview = (props) => {
    // 取得必要属性或参数
    const {
        id,
        style,
        className,
        src,
        setProps,
        loading_state
    } = props;

    const containerRef = useRef(null);

    useEffect(
        () => {
            if (!containerRef.current) return;

            // 挂载到指定目标容器
            const wordPreviewer = jsPreviewDocx.init(
                containerRef.current,
                {
                }
            );

            // 传递要预览的文件地址即可
            wordPreviewer.preview(src).then(res => {
                // console.log('预览完成');
            }).catch(e => {
                // console.log('预览失败', e);
            });

            // 清除资源（在组件卸载时）
            return () => {
                wordPreviewer.destroy();
            };
        }, [src]
    )

    return (
        <div
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            ref={containerRef}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyWordPreview;

FefferyWordPreview.defaultProps = defaultProps;
FefferyWordPreview.propTypes = propTypes;