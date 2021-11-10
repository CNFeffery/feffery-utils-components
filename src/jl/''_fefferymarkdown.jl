# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferymarkdown

"""
    ''_fefferymarkdown(;kwargs...)

A FefferyMarkdown component.

Keyword arguments:
- `id` (String; optional)
- `codeStyle` (String; optional)
- `linkTarget` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `markdownStr` (String; optional)
- `renderHtml` (Bool; optional)
"""
function ''_fefferymarkdown(; kwargs...)
        available_props = Symbol[:id, :codeStyle, :linkTarget, :loading_state, :markdownStr, :renderHtml]
        wild_props = Symbol[]
        return Component("''_fefferymarkdown", "FefferyMarkdown", "feffery_utils_components", available_props, wild_props; kwargs...)
end

