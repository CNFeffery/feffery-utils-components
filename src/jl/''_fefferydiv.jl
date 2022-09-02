# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferydiv

"""
    ''_fefferydiv(;kwargs...)
    ''_fefferydiv(children::Any;kwargs...)
    ''_fefferydiv(children_maker::Function;kwargs...)


A FefferyDiv component.

Keyword arguments:
- `children` (optional)
- `id` (optional)
- `_height` (optional)
- `_width` (optional)
- `className` (optional)
- `contextMenuEvent` (optional)
- `debounceWait` (optional)
- `enableListenContextMenu` (optional)
- `loading_state` (optional)
- `mouseEnterCounts` (optional)
- `mouseLeaveCounts` (optional)
- `nClicks` (optional)
- `nDoubleClicks` (optional)
- `setProps` (optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `style` (optional)
"""
function ''_fefferydiv(; kwargs...)
        available_props = Symbol[:children, :id, :_height, :_width, :className, :contextMenuEvent, :debounceWait, :enableListenContextMenu, :loading_state, :mouseEnterCounts, :mouseLeaveCounts, :nClicks, :nDoubleClicks, :style]
        wild_props = Symbol[]
        return Component("''_fefferydiv", "FefferyDiv", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferydiv(children::Any; kwargs...) = ''_fefferydiv(;kwargs..., children = children)
''_fefferydiv(children_maker::Function; kwargs...) = ''_fefferydiv(children_maker(); kwargs...)

