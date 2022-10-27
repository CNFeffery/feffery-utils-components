# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyeyedropper

"""
    ''_fefferyeyedropper(;kwargs...)

A FefferyEyeDropper component.

Keyword arguments:
- `id` (String; optional)
- `color` (String; optional)
- `enable` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function ''_fefferyeyedropper(; kwargs...)
        available_props = Symbol[:id, :color, :enable, :loading_state]
        wild_props = Symbol[]
        return Component("''_fefferyeyedropper", "FefferyEyeDropper", "feffery_utils_components", available_props, wild_props; kwargs...)
end

