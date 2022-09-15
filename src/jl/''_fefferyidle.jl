# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyidle

"""
    ''_fefferyidle(;kwargs...)

A FefferyIdle component.

Keyword arguments:
- `id` (String; optional)
- `isIdle` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `waitDuration` (Real; optional)
"""
function ''_fefferyidle(; kwargs...)
        available_props = Symbol[:id, :isIdle, :loading_state, :waitDuration]
        wild_props = Symbol[]
        return Component("''_fefferyidle", "FefferyIdle", "feffery_utils_components", available_props, wild_props; kwargs...)
end

