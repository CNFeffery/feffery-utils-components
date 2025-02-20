// react核心
import { useRef, useEffect } from 'react';
// 组件核心
import jsPreviewDocx from "@js-preview/docx";
// 样式
import '@js-preview/docx/lib/index.css';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/filePreview/FefferyWordPreview.react';

/**
 * word文件预览组件FefferyWordPreview
 */
const FefferyWordPreview = ({
    id,
    style,
    className,
    src,
    setProps
}) => {

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
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyWordPreview;

FefferyWordPreview.defaultProps = defaultProps;
FefferyWordPreview.propTypes = propTypes;