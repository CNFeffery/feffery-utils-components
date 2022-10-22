# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferystyle

"""
    ''_fefferystyle(;kwargs...)

A FefferyStyle component.

Keyword arguments:
- `id` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `rawStyle` (String; optional)
"""
function ''_fefferystyle(; kwargs...)
        available_props = Symbol[:id, :loading_state, :rawStyle]
        wild_props = Symbol[]
        return Component("''_fefferystyle", "FefferyStyle", "feffery_utils_components", available_props, wild_props; kwargs...)
end

