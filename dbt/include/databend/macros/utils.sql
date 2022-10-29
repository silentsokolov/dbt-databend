{% macro databend__any_value(expression) -%}
    any({{ expression }})
{%- endmacro %}