
{% macro remove_linebreaks (col) %}
    regexp_replace({{col}}, '[\n\r]', '', 'g')
{% endmacro %}
