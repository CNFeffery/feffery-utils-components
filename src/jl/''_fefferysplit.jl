# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysplit

"""
    ''_fefferysplit(;kwargs...)
    ''_fefferysplit(children::Any;kwargs...)
    ''_fefferysplit(children_maker::Function;kwargs...)


A FefferySplit component.

Keyword arguments:
- `children` (optional)
- `id` (optional)
- `className` (optional)
- `cursor` (optional)
- `direction` (optional)
- `dragInterval` (optional)
- `expandToMin` (optional)
- `gutterSize` (optional)
- `loading_state` (optional)
- `maxSize` (optional)
- `minSize` (optional)
- `setProps` (optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `sizes` (optional)
- `style` (optional)
"""
function ''_fefferysplit(; kwargs...)
        available_props = Symbol[:children, :id, :className, :cursor, :direction, :dragInterval, :expandToMin, :gutterSize, :loading_state, :maxSize, :minSize, :sizes, :style]
        wild_props = Symbol[]
        return Component("''_fefferysplit", "FefferySplit", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferysplit(children::Any; kwargs...) = ''_fefferysplit(;kwargs..., children = children)
''_fefferysplit(children_maker::Function; kwargs...) = ''_fefferysplit(children_maker(); kwargs...)

