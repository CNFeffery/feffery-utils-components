# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferytimeout

"""
    ''_fefferytimeout(;kwargs...)

A FefferyTimeout component.

Keyword arguments:
- `id` (String; optional)
- `delay` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `timeoutCount` (Real; optional)
"""
function ''_fefferytimeout(; kwargs...)
        available_props = Symbol[:id, :delay, :loading_state, :timeoutCount]
        wild_props = Symbol[]
        return Component("''_fefferytimeout", "FefferyTimeout", "feffery_utils_components", available_props, wild_props; kwargs...)
end

