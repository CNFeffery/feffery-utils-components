# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferylazyload

"""
    ''_fefferylazyload(;kwargs...)
    ''_fefferylazyload(children::Any;kwargs...)
    ''_fefferylazyload(children_maker::Function;kwargs...)


A FefferyLazyLoad component.

Keyword arguments:
- `children` (optional)
- `id` (optional)
- `className` (optional)
- `height` (optional)
- `loading_state` (optional)
- `offset` (optional)
- `setProps` (optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `style` (optional)
- `throttle` (optional)
- `visible` (optional)
- `width` (optional)
"""
function ''_fefferylazyload(; kwargs...)
        available_props = Symbol[:children, :id, :className, :height, :loading_state, :offset, :style, :throttle, :visible, :width]
        wild_props = Symbol[]
        return Component("''_fefferylazyload", "FefferyLazyLoad", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferylazyload(children::Any; kwargs...) = ''_fefferylazyload(;kwargs..., children = children)
''_fefferylazyload(children_maker::Function; kwargs...) = ''_fefferylazyload(children_maker(); kwargs...)

