# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyimagepaste

"""
    ''_fefferyimagepaste(;kwargs...)

A FefferyImagePaste component.

Keyword arguments:
- `id` (String; optional)
- `disabled` (Bool; optional)
- `imageInfo` (optional): . imageInfo has the following type: lists containing elements 'base64', 'timestamp'.
Those elements have the following types:
  - `base64` (String; optional)
  - `timestamp` (Real; optional)
- `key` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function ''_fefferyimagepaste(; kwargs...)
        available_props = Symbol[:id, :disabled, :imageInfo, :key, :loading_state]
        wild_props = Symbol[]
        return Component("''_fefferyimagepaste", "FefferyImagePaste", "feffery_utils_components", available_props, wild_props; kwargs...)
end

