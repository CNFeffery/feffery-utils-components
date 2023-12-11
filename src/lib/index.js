/* eslint-disable import/prefer-default-export */
import FefferyCaptcha from "./components/FefferyCaptcha.react";
import FefferyTopProgress from "./components/FefferyTopProgress.react";
import FefferyShortcutPanel from "./components/FefferyShortcutPanel.react";
import FefferyGuide from "./components/FefferyGuide.react";
import FefferyExecuteJs from "./components/FefferyExecuteJs.react";
import FefferyScroll from "./components/FefferyScroll.react";
import FefferyScrollbars from "./components/FefferyScrollbars.react";
import FefferyExtraSpinner from "./components/FefferyExtraSpinner.react";
import FefferyLazyLoad from "./components/FefferyLazyLoad.react";
import FefferyVirtualList from "./components/FefferyVirtualList.react";
import FefferyInViewport from "./components/listeners/FefferyInViewport.react";
import FefferyHexColorPicker from "./components/colorPickers/FefferyHexColorPicker.react";
import FefferyRgbColorPicker from "./components/colorPickers/FefferyRgbColorPicker.react";
import FefferyGithubColorPicker from "./components/colorPickers/FefferyGithubColorPicker.react";
import FefferyTwitterColorPicker from "./components/colorPickers/FefferyTwitterColorPicker.react";
import FefferyBlockColorPicker from "./components/colorPickers/FefferyBlockColorPicker.react";
import FefferyCircleColorPicker from "./components/colorPickers/FefferyCircleColorPicker.react";
import FefferyWheelColorPicker from "./components/colorPickers/FefferyWheelColorPicker.react";
import FefferyHighlightWords from "./components/FefferyHighlightWords.react";
import FefferyDocumentVisibility from "./components/listeners/FefferyDocumentVisibility.react";
import FefferyExternalCss from "./components/FefferyExternalCss.react";
import FefferyExternalJs from "./components/FefferyExternalJs.react";
import FefferySetTitle from "./components/FefferySetTitle.react";
import FefferyResponsive from "./components/listeners/FefferyResponsive.react";
import FefferyGeolocation from "./components/listeners/FefferyGeolocation.react";
import FefferyIdle from "./components/listeners/FefferyIdle.react";
import FefferyWindowSize from "./components/listeners/FefferyWindowSize.react";
import FefferyKeyPress from "./components/listeners/FefferyKeyPress.react";
import FefferyTimeout from "./components/FefferyTimeout.react";
import FefferyCountDown from "./components/FefferyCountDown.react";
import FefferyRawHTML from "./components/FefferyRawHTML.react";
import FefferyFancyNotification from "./components/FefferyFancyNotification";
import FefferyQRCode from "./components/FefferyQrcode.react";
import FefferyFancyMessage from "./components/FefferyFancyMessage";
import FefferyStyle from "./components/FefferyStyle.react";
import FefferyDiv from "./components/FefferyDiv.react";
import FefferyReload from "./components/FefferyReload.react";
import FefferyCssVar from "./components/FefferyCssVar.react";
import FefferyEyeDropper from "./components/colorPickers/FefferyEyeDropper.react";
import FefferySticky from "./components/FefferySticky.react";
import FefferySessionStorage from "./components/store/FefferySessionStorage.react";
import FefferyWebSocket from "./components/FefferyWebSocket.react";
import FefferyShadowDom from "./components/FefferyShadowDom.react";
import FefferyGrid from "./components/draggable/FefferyGrid.react";
import FefferyGridItem from "./components/draggable/FefferyGridItem.react";
import FefferyFancyButton from "./components/FefferyFancyButton.react";
import FefferyJsonViewer from "./components/FefferyJsonViewer.react";
import FefferyImagePaste from "./components/FefferyImagePaste.react";
import FefferyFullscreen from "./components/FefferyFullscreen.react";
import FefferyDeviceDetect from "./components/listeners/FefferyDeviceDetect.react";
import FefferyMotion from "./components/animations/FefferyMotion.react";
import FefferyAutoAnimate from "./components/animations/FefferyAutoAnimate.react";
import FefferyCountUp from "./components/FefferyCountUp.react";
import FefferyListenUnload from "./components/listeners/FefferyListenUnload.react";
import FefferyListenScroll from "./components/listeners/FefferyListenScroll.react";
import FefferyMousePosition from "./components/listeners/FefferyMousePosition.react";
import FefferyListenPaste from "./components/listeners/FefferyListenPaste.react";
import FefferyLocation from "./components/listeners/FefferyLocation.react";
import FefferyCookie from "./components/store/FefferyCookie.react";
import FefferyResizable from "./components/resizable/FefferyResizable.react";
import FefferyCompareSlider from "./components/FefferyCompareSlider.react";
import FefferySortableList from "./components/sortable/FefferySortableList.react";
import FefferyLocalStorage from "./components/store/FefferyLocalStorage.react";
import FefferyTextSelection from "./components/listeners/FefferyTextSelection.react";
import FefferyLocalLargeStorage from "./components/store/FefferyLocalLargeStorage.react";
import FefferyLongPress from "./components/listeners/FefferyLongPress.react";
import FefferyDebounceProp from "./components/store/FefferyDebounceProp.react";
import FefferyMusicPlayer from "./components/player/FefferyMusicPlayer.react";
import FefferyAPlayer from "./components/player/FefferyAPlayer.react";
import FefferyDPlayer from "./components/player/FefferyDPlayer.react";
import FefferyThrottleProp from "./components/store/FefferyThrottleProp.react";
import FefferyTabMessenger from "./components/FefferyTabMessenger.react";
import FefferyEmojiPicker from "./components/FefferyEmojiPicker.react";
import FefferyAutoFit from "./components/resizable/FefferyAutoFit.react";
import FefferyRichTextEditor from "./components/FefferyRichTextEditor.react";
import FefferyImageGallery from "./components/images/FefferyImageGallery.react";
import './components/styles.css';

// 自定义sessionStorage事件监听
const originalSessionSetItem = sessionStorage.setItem;
sessionStorage.setItem = function (key, newValue) {
    originalSessionSetItem.apply(this, [key, newValue]);
    const setItemEvent = new Event("sessionStorageSetItem");
    setItemEvent['triggerKey'] = key
    setItemEvent[key] = newValue;
    window.dispatchEvent(setItemEvent);
};

// 自定义localStorage事件监听
const originalLocalSetItem = localStorage.setItem;
localStorage.setItem = function (key, newValue) {
    originalLocalSetItem.apply(this, [key, newValue]);
    const setItemEvent = new Event("localStorageSetItem");
    setItemEvent['triggerKey'] = key
    setItemEvent[key] = newValue;
    window.dispatchEvent(setItemEvent);
};


export {
    FefferyCaptcha,
    FefferyTopProgress,
    FefferyShortcutPanel,
    FefferyGuide,
    FefferyExecuteJs,
    FefferyScroll,
    FefferyScrollbars,
    FefferyExtraSpinner,
    FefferyLazyLoad,
    FefferyVirtualList,
    FefferyInViewport,
    FefferyHexColorPicker,
    FefferyRgbColorPicker,
    FefferyGithubColorPicker,
    FefferyTwitterColorPicker,
    FefferyBlockColorPicker,
    FefferyCircleColorPicker,
    FefferyWheelColorPicker,
    FefferyHighlightWords,
    FefferyDocumentVisibility,
    FefferyExternalCss,
    FefferyExternalJs,
    FefferySetTitle,
    FefferyResponsive,
    FefferyGeolocation,
    FefferyIdle,
    FefferyWindowSize,
    FefferyKeyPress,
    FefferyTimeout,
    FefferyCountDown,
    FefferyRawHTML,
    FefferyFancyNotification,
    FefferyQRCode,
    FefferyFancyMessage,
    FefferyStyle,
    FefferyDiv,
    FefferyReload,
    FefferyCssVar,
    FefferyEyeDropper,
    FefferySticky,
    FefferySessionStorage,
    FefferyWebSocket,
    FefferyShadowDom,
    FefferyGrid,
    FefferyGridItem,
    FefferyFancyButton,
    FefferyJsonViewer,
    FefferyImagePaste,
    FefferyFullscreen,
    FefferyDeviceDetect,
    FefferyMotion,
    FefferyAutoAnimate,
    FefferyCountUp,
    FefferyListenUnload,
    FefferyListenScroll,
    FefferyMousePosition,
    FefferyListenPaste,
    FefferyLocation,
    FefferyCookie,
    FefferyResizable,
    FefferyCompareSlider,
    FefferySortableList,
    FefferyLocalStorage,
    FefferyTextSelection,
    FefferyLocalLargeStorage,
    FefferyLongPress,
    FefferyDebounceProp,
    FefferyMusicPlayer,
    FefferyAPlayer,
    FefferyDPlayer,
    FefferyThrottleProp,
    FefferyTabMessenger,
    FefferyEmojiPicker,
    FefferyAutoFit,
    FefferyRichTextEditor,
    FefferyImageGallery
};