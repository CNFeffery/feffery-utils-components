# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferydiv

"""
    ''_fefferydiv(;kwargs...)
    ''_fefferydiv(children::Any;kwargs...)
    ''_fefferydiv(children_maker::Function;kwargs...)


A FefferyDiv component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `_height` (Real; optional)
- `_width` (Real; optional)
- `className` (String | Dict; optional)
- `clickAwayCount` (Real; optional)
- `contextMenuEvent` (optional): . contextMenuEvent has the following type: lists containing elements 'pageX', 'pageY', 'clientX', 'clientY', 'screenX', 'screenY', 'timestamp'.
Those elements have the following types:
  - `pageX` (Real; optional)
  - `pageY` (Real; optional)
  - `clientX` (Real; optional)
  - `clientY` (Real; optional)
  - `screenX` (Real; optional)
  - `screenY` (Real; optional)
  - `timestamp` (Real; optional)
- `debounceWait` (Real; optional)
- `enableClickAway` (Bool; optional)
- `enableListenContextMenu` (Bool; optional)
- `enableListenPaste` (Bool; optional)
- `isHovering` (Bool; optional)
- `key` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `mouseEnterCount` (Real; optional)
- `mouseLeaveCount` (Real; optional)
- `nClicks` (Real; optional)
- `nDoubleClicks` (Real; optional)
- `pasteCount` (Real; optional)
- `pasteText` (String; optional)
- `scrollbar` (a value equal to: 'default', 'simple', 'hidden'; optional)
- `shadow` (a value equal to: 'no-shadow', 'hover-shadow', 'always-shadow'; optional)
- `style` (Dict; optional)
"""
function ''_fefferydiv(; kwargs...)
        available_props = Symbol[:children, :id, :_height, :_width, :className, :clickAwayCount, :contextMenuEvent, :debounceWait, :enableClickAway, :enableListenContextMenu, :enableListenPaste, :isHovering, :key, :loading_state, :mouseEnterCount, :mouseLeaveCount, :nClicks, :nDoubleClicks, :pasteCount, :pasteText, :scrollbar, :shadow, :style]
        wild_props = Symbol[]
        return Component("''_fefferydiv", "FefferyDiv", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferydiv(children::Any; kwargs...) = ''_fefferydiv(;kwargs..., children = children)
''_fefferydiv(children_maker::Function; kwargs...) = ''_fefferydiv(children_maker(); kwargs...)

