# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyscroll

"""
    ''_fefferyscroll(;kwargs...)

A FefferyScroll component.

Keyword arguments:
- `id` (String; optional)
- `containerId` (String; optional)
- `delay` (Real; optional)
- `duration` (Real; optional)
- `executeScroll` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `offset` (Real; optional)
- `scrollMode` (a value equal to: 'to-top', 'to-bottom', 'top-offset', 'relative-offset', 'target'; optional)
- `scrollRelativeOffset` (Real; optional)
- `scrollTargetId` (String; optional)
- `scrollTopOffset` (Real; optional)
- `smooth` (Bool | a value equal to: 'linear', 'easeInQuad', 'easeOutQuad', 'easeInOutQuad', 'easeInCubic', 'easeOutCubic', 'easeInOutCubic', 'easeInQuart', 'easeOutQuart', 'easeInOutQuart', 'easeInQuint', 'easeOutQuint', 'easeInOutQuint'; optional)
"""
function ''_fefferyscroll(; kwargs...)
        available_props = Symbol[:id, :containerId, :delay, :duration, :executeScroll, :loading_state, :offset, :scrollMode, :scrollRelativeOffset, :scrollTargetId, :scrollTopOffset, :smooth]
        wild_props = Symbol[]
        return Component("''_fefferyscroll", "FefferyScroll", "feffery_utils_components", available_props, wild_props; kwargs...)
end

