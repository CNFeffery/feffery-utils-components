# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyfancymessage

"""
    ''_fefferyfancymessage(;kwargs...)
    ''_fefferyfancymessage(children::Any;kwargs...)
    ''_fefferyfancymessage(children_maker::Function;kwargs...)


A FefferyFancyMessage component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `containerClassName` (String; optional)
- `containerStyle` (Dict; optional)
- `duration` (Real; optional)
- `gutter` (Real; optional)
- `icon` (a list of or a singular dash component, string or number; optional)
- `key` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `position` (a value equal to: 'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'; optional)
- `reverseOrder` (Bool; optional)
- `style` (Dict; optional)
- `type` (a value equal to: 'blank', 'success', 'error'; optional)
- `visible` (Bool; optional)
"""
function ''_fefferyfancymessage(; kwargs...)
        available_props = Symbol[:children, :id, :className, :containerClassName, :containerStyle, :duration, :gutter, :icon, :key, :loading_state, :position, :reverseOrder, :style, :type, :visible]
        wild_props = Symbol[]
        return Component("''_fefferyfancymessage", "FefferyFancyMessage", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyfancymessage(children::Any; kwargs...) = ''_fefferyfancymessage(;kwargs..., children = children)
''_fefferyfancymessage(children_maker::Function; kwargs...) = ''_fefferyfancymessage(children_maker(); kwargs...)

