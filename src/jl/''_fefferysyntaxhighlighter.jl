# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysyntaxhighlighter

"""
    ''_fefferysyntaxhighlighter(;kwargs...)

A FefferySyntaxHighlighter component.

Keyword arguments:
- `id` (String; optional)
- `codeString` (String; required)
- `codeStyle` (String; optional)
- `language` (String; required)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `showInlineLineNumbers` (Bool; optional)
- `showLineNumbers` (Bool; optional)
"""
function ''_fefferysyntaxhighlighter(; kwargs...)
        available_props = Symbol[:id, :codeString, :codeStyle, :language, :loading_state, :showInlineLineNumbers, :showLineNumbers]
        wild_props = Symbol[]
        return Component("''_fefferysyntaxhighlighter", "FefferySyntaxHighlighter", "feffery_utils_components", available_props, wild_props; kwargs...)
end

