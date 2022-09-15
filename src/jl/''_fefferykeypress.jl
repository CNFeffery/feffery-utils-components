# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferykeypress

"""
    ''_fefferykeypress(;kwargs...)

A FefferyKeyPress component.

Keyword arguments:
- `id` (String; optional)
- `keys` (String; required)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `pressedTimes` (Real; optional)
"""
function ''_fefferykeypress(; kwargs...)
        available_props = Symbol[:id, :keys, :loading_state, :pressedTimes]
        wild_props = Symbol[]
        return Component("''_fefferykeypress", "FefferyKeyPress", "feffery_utils_components", available_props, wild_props; kwargs...)
end

