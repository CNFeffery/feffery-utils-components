# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferydevicedetect

"""
    ''_fefferydevicedetect(;kwargs...)

A FefferyDeviceDetect component.

Keyword arguments:
- `id` (String; optional)
- `deviceInfo` (optional): . deviceInfo has the following type: lists containing elements 'isMobile', 'isAndroid', 'isIOS', 'isChrome', 'isFirefox', 'isSafari', 'isIE', 'isEdge', 'osVersion', 'osName', 'browserVersion', 'fullBrowserVersion', 'browserName', 'ua', 'deviceType'.
Those elements have the following types:
  - `isMobile` (Bool; optional)
  - `isAndroid` (Bool; optional)
  - `isIOS` (Bool; optional)
  - `isChrome` (Bool; optional)
  - `isFirefox` (Bool; optional)
  - `isSafari` (Bool; optional)
  - `isIE` (Bool; optional)
  - `isEdge` (Bool; optional)
  - `osVersion` (String; optional)
  - `osName` (String; optional)
  - `browserVersion` (String; optional)
  - `fullBrowserVersion` (String; optional)
  - `browserName` (String; optional)
  - `ua` (String; optional)
  - `deviceType` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function ''_fefferydevicedetect(; kwargs...)
        available_props = Symbol[:id, :deviceInfo, :loading_state]
        wild_props = Symbol[]
        return Component("''_fefferydevicedetect", "FefferyDeviceDetect", "feffery_utils_components", available_props, wild_props; kwargs...)
end

