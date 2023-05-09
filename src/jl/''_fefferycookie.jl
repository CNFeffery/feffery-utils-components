# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferycookie

"""
    ''_fefferycookie(;kwargs...)

A FefferyCookie component.

Keyword arguments:
- `id` (String; optional)
- `cookieKey` (String; required)
- `defaultValue` (String; optional)
- `expires` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `pathname` (String; optional)
- `secure` (Bool; optional)
- `value` (String; optional)
"""
function ''_fefferycookie(; kwargs...)
        available_props = Symbol[:id, :cookieKey, :defaultValue, :expires, :loading_state, :pathname, :secure, :value]
        wild_props = Symbol[]
        return Component("''_fefferycookie", "FefferyCookie", "feffery_utils_components", available_props, wild_props; kwargs...)
end

