# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyshortcutpanel

"""
    ''_fefferyshortcutpanel(;kwargs...)

A FefferyShortcutPanel component.

Keyword arguments:
- `id` (String; optional)
- `close` (Bool; optional)
- `data` (required): . data has the following type: Array of lists containing elements 'id', 'title', 'hotkey', 'handler', 'parent', 'keywords', 'children', 'section'.
Those elements have the following types:
  - `id` (String; required)
  - `title` (String; required)
  - `hotkey` (String; optional)
  - `handler` (String; optional)
  - `parent` (String; optional)
  - `keywords` (String; optional)
  - `children` (Array of Strings; optional)
  - `section` (String; optional)s
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'en', 'zh'; optional)
- `open` (Bool; optional)
- `openHotkey` (String; optional)
- `placeholder` (String; optional)
- `theme` (a value equal to: 'light', 'dark'; optional)
- `triggeredHotkey` (optional): . triggeredHotkey has the following type: lists containing elements 'id', 'timestamp'.
Those elements have the following types:
  - `id` (String; optional)
  - `timestamp` (Real; optional)
"""
function ''_fefferyshortcutpanel(; kwargs...)
        available_props = Symbol[:id, :close, :data, :loading_state, :locale, :open, :openHotkey, :placeholder, :theme, :triggeredHotkey]
        wild_props = Symbol[]
        return Component("''_fefferyshortcutpanel", "FefferyShortcutPanel", "feffery_utils_components", available_props, wild_props; kwargs...)
end

