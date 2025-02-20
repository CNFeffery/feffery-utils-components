// react核心
import React, { useMemo } from 'react';
// 组件核心
import data from '@emoji-mart/data';
import Picker from '@emoji-mart/react';
import en from '@emoji-mart/data/i18n/en.json';
import zh from '@emoji-mart/data/i18n/zh.json';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/dataInput/FefferyEmojiPicker.react';

/**
 * emoji选择器组件FefferyEmojiPicker
 */
const FefferyEmojiPicker = (props) => {
    let {
        id,
        key,
        style,
        className,
        locale,
        categories,
        custom,
        customCategoryIcons,
        autoFocus,
        dynamicWidth,
        perLine,
        emojiButtonColors,
        emojiButtonRadius,
        emojiButtonSize,
        emojiSize,
        emojiVersion,
        exceptEmojis,
        icons,
        maxFrequentRows,
        navPosition,
        noResultsEmoji,
        previewEmoji,
        previewPosition,
        searchPosition,
        set,
        skin,
        skinTonePosition,
        theme,
        value,
        clickOutsideNums,
        setProps
    } = props;

    const i18n = useMemo(() => {
        switch (locale) {
            case 'en':
                return en;
            case 'zh':
                return zh;
            default:
                return zh;
        }
    }, [locale])

    return (
        <div>
            <Picker
                id={id}
                key={key}
                style={style}
                className={className}
                i18n={i18n}
                data={data}
                categories={categories}
                custom={custom}
                customCategoryIcons={customCategoryIcons}
                autoFocus={autoFocus}
                dynamicWidth={dynamicWidth}
                perLine={perLine}
                emojiButtonColors={emojiButtonColors}
                emojiButtonRadius={emojiButtonRadius}
                emojiButtonSize={emojiButtonSize}
                emojiSize={emojiSize}
                emojiVersion={emojiVersion}
                exceptEmojis={exceptEmojis}
                icons={icons}
                maxFrequentRows={maxFrequentRows}
                navPosition={navPosition}
                noResultsEmoji={noResultsEmoji}
                previewEmoji={previewEmoji}
                previewPosition={previewPosition}
                searchPosition={searchPosition}
                set={set}
                skin={skin}
                skinTonePosition={skinTonePosition}
                theme={theme}
                onEmojiSelect={e => setProps({ value: { ...e, timestamp: Date.parse(new Date()) } })}
                onClickOutside={() => setProps({ clickOutsideNums: clickOutsideNums + 1 })}
                data-dash-is-loading={useLoading()}
            />
        </div>
    );
}

export default FefferyEmojiPicker;

FefferyEmojiPicker.defaultProps = defaultProps;
FefferyEmojiPicker.propTypes = propTypes;