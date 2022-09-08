# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyhighlightwords

"""
    ''_fefferyhighlightwords(;kwargs...)

A FefferyHighlightWords component.

Keyword arguments:
- `id` (String; optional)
- `caseSensitive` (Bool; optional)
- `className` (String; optional)
- `highlightClassName` (String; optional)
- `highlightStyle` (Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `searchWords` (Array of Strings; optional)
- `style` (Dict; optional)
- `textToHighlight` (String; optional)
- `unhighlightClassName` (String; optional)
- `unhighlightStyle` (Dict; optional)
- `useRegex` (Bool; optional)
"""
function ''_fefferyhighlightwords(; kwargs...)
        available_props = Symbol[:id, :caseSensitive, :className, :highlightClassName, :highlightStyle, :loading_state, :searchWords, :style, :textToHighlight, :unhighlightClassName, :unhighlightStyle, :useRegex]
        wild_props = Symbol[]
        return Component("''_fefferyhighlightwords", "FefferyHighlightWords", "feffery_utils_components", available_props, wild_props; kwargs...)
end

