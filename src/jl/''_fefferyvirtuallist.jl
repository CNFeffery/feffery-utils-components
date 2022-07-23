# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyvirtuallist

"""
    ''_fefferyvirtuallist(;kwargs...)
    ''_fefferyvirtuallist(children::Any;kwargs...)
    ''_fefferyvirtuallist(children_maker::Function;kwargs...)


A FefferyVirtualList component.

Keyword arguments:
- `children` (optional)
- `id` (optional)
- `className` (optional)
- `height` (optional)
- `itemHeight` (optional)
- `loading_state` (optional)
- `setProps` (optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `style` (optional)
"""
function ''_fefferyvirtuallist(; kwargs...)
        available_props = Symbol[:children, :id, :className, :height, :itemHeight, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferyvirtuallist", "FefferyVirtualList", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyvirtuallist(children::Any; kwargs...) = ''_fefferyvirtuallist(;kwargs..., children = children)
''_fefferyvirtuallist(children_maker::Function; kwargs...) = ''_fefferyvirtuallist(children_maker(); kwargs...)

