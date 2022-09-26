# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysortableitem

"""
    ''_fefferysortableitem(;kwargs...)
    ''_fefferysortableitem(children::Any;kwargs...)
    ''_fefferysortableitem(children_maker::Function;kwargs...)


A FefferySortableItem component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function ''_fefferysortableitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferysortableitem", "FefferySortableItem", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferysortableitem(children::Any; kwargs...) = ''_fefferysortableitem(;kwargs..., children = children)
''_fefferysortableitem(children_maker::Function; kwargs...) = ''_fefferysortableitem(children_maker(); kwargs...)

