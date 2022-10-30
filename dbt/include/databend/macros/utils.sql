{% macro databend__any_value(expression) -%}
    any({{ expression }})
{%- endmacro %}

{% macro databend__dateadd(datepart, interval, from_date_or_timestamp) %}
    date_add(
        {{ datepart }},
        {{ interval }},
        {{ from_date_or_timestamp }}
        )
{% endmacro %}