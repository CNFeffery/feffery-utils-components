import React, { useMemo, useEffect, useRef } from 'react';
import data from '@emoji-mart/data';
import Picker from '@emoji-mart/react';
import en from '@emoji-mart/data/i18n/en.json';
import zh from '@emoji-mart/data/i18n/zh.json';
import { propTypes, defaultProps } from '../components/FefferyEmojiPicker.react';

// 定义emoji选择器组件FefferyEmojiPicker，api参数参考https://github.com/missive/emoji-mart#-picker
const FefferyEmojiPicker = (props) => {
    // 取得必要属性或参数
    let {
        id,
        className,
        style,
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
        setProps,
        loading_state
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
                className={className}
                style={style}
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
                onEmojiSelect={e => setProps({ value: e})}
                onClickOutside={() => setProps({ clickOutsideNums: clickOutsideNums + 1})}
                loading_state={loading_state}
            />
        </div>
    );
}

export default FefferyEmojiPicker;

FefferyEmojiPicker.defaultProps = defaultProps;
FefferyEmojiPicker.propTypes = propTypes;