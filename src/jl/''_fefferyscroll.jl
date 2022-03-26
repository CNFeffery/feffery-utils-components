# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyscroll

"""
    ''_fefferyscroll(;kwargs...)

A FefferyScroll component.

Keyword arguments:
- `id` (optional)
- `containerId` (optional)
- `delay` (optional)
- `duration` (optional)
- `executeScroll` (optional)
- `loading_state` (optional)
- `offset` (optional)
- `scrollMode` (optional)
- `scrollRelativeOffset` (optional)
- `scrollTargetId` (optional)
- `scrollTopOffset` (optional)
- `setProps` (optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `smooth` (optional)
"""
function ''_fefferyscroll(; kwargs...)
        available_props = Symbol[:id, :containerId, :delay, :duration, :executeScroll, :loading_state, :offset, :scrollMode, :scrollRelativeOffset, :scrollTargetId, :scrollTopOffset, :smooth]
        wild_props = Symbol[]
        return Component("''_fefferyscroll", "FefferyScroll", "feffery_utils_components", available_props, wild_props; kwargs...)
end

