/* eslint-disable import/prefer-default-export */
import FefferyCaptcha from "./components/FefferyCaptcha.react"; // 待异步优化
import FefferyTopProgress from "./components/FefferyTopProgress.react";
import FefferyShortcutPanel from "./components/FefferyShortcutPanel.react"; // 待异步优化
import FefferyGuide from "./components/FefferyGuide.react";
import FefferySplit from "./components/split/FefferySplit.react";
import FefferySplitPane from "./components/split/FefferySplitPane.react";
import FefferyExecuteJs from "./components/FefferyExecuteJs.react";
import FefferyScroll from "./components/FefferyScroll.react";
import FefferyScrollbars from "./components/FefferyScrollbars.react";
import FefferyExtraSpinner from "./components/FefferyExtraSpinner.react"; // 待异步优化
import FefferyLazyLoad from "./components/FefferyLazyLoad.react";
import FefferyVirtualList from "./components/FefferyVirtualList.react";
import FefferyInViewport from "./components/listeners/FefferyInViewport.react";
import FefferyHexColorPicker from "./components/colorPickers/FefferyHexColorPicker.react"; // 待异步优化
import FefferyRgbColorPicker from "./components/colorPickers/FefferyRgbColorPicker.react"; // 待异步优化
import FefferyGithubColorPicker from "./components/colorPickers/FefferyGithubColorPicker.react"; // 待异步优化
import FefferyTwitterColorPicker from "./components/colorPickers/FefferyTwitterColorPicker.react"; // 待异步优化
import FefferyBlockColorPicker from "./components/colorPickers/FefferyBlockColorPicker.react"; // 待异步优化
import FefferyCircleColorPicker from "./components/colorPickers/FefferyCircleColorPicker.react"; // 待异步优化
import FefferyWheelColorPicker from "./components/colorPickers/FefferyWheelColorPicker.react"; // 待异步优化
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
import FefferyGrid from "./components/draggable/FefferyGrid.react"; // 待异步优化
import FefferyGridItem from "./components/draggable/FefferyGridItem.react"; // 待异步优化
import FefferyFancyButton from "./components/FefferyFancyButton.react"; // 待异步优化
import FefferyJsonViewer from "./components/FefferyJsonViewer.react"; // 待异步优化
import FefferyImagePaste from "./components/FefferyImagePaste.react";
import FefferyFullscreen from "./components/FefferyFullscreen.react";
import FefferyDeviceDetect from "./components/listeners/FefferyDeviceDetect.react";
import FefferyMotion from "./components/animations/FefferyMotion.react";
import FefferyAutoAnimate from "./components/animations/FefferyAutoAnimate.react"; // 待异步优化
import FefferyCountUp from "./components/FefferyCountUp.react";
import FefferyListenUnload from "./components/listeners/FefferyListenUnload.react";
import FefferyListenScroll from "./components/listeners/FefferyListenScroll.react";
import FefferyMousePosition from "./components/listeners/FefferyMousePosition.react";
import FefferyListenPaste from "./components/listeners/FefferyListenPaste.react";
import FefferyLocation from "./components/listeners/FefferyLocation.react";
import FefferyCookie from "./components/store/FefferyCookie.react";
import FefferyResizable from "./components/resizable/FefferyResizable.react"; // 待异步优化
import FefferyCompareSlider from "./components/FefferyCompareSlider.react";
import FefferySortableList from "./components/sortable/FefferySortableList.react"; // 待异步优化
import FefferyLocalStorage from "./components/store/FefferyLocalStorage.react";
import FefferyTextSelection from "./components/listeners/FefferyTextSelection.react";
import FefferyLocalLargeStorage from "./components/store/FefferyLocalLargeStorage.react"; // 待异步优化
import FefferyLongPress from "./components/listeners/FefferyLongPress.react";
import FefferyDebounceProp from "./components/store/FefferyDebounceProp.react";
import FefferyMusicPlayer from "./components/player/FefferyMusicPlayer.react"; // 待异步优化
import FefferyAPlayer from "./components/player/FefferyAPlayer.react"; // 待异步优化
import FefferyDPlayer from "./components/player/FefferyDPlayer.react"; // 待异步优化
import FefferyThrottleProp from "./components/store/FefferyThrottleProp.react";


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
    FefferySplit,
    FefferySplitPane,
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
    FefferyThrottleProp
};