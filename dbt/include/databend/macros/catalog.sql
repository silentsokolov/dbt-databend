{% macro databend__get_catalog(information_schema, schemas) -%}
  {%- call statement('planner') -%}
    set enable_planner_v2 = 1;
  {%- endcall -%}
  {%- call statement('catalog', fetch_result=True) -%}
    select
      null as table_database,
      tables.database as table_schema,
      tables.name as table_name,
      if(tables.engine = 'VIEW', 'view', 'table') as table_type,
      null as table_comment,
      columns.name as column_name,
      0 as column_index,
      columns.type as column_type,
      columns.comment as column_comment,
      null as table_owner
    from system.columns as columns
    join system.tables as tables on tables.database = columns.database and tables.name = columns.table
    where tables.database != 'system' and
    (
    {%- for schema in schemas -%}
      tables.database = '{{ schema }}'
      {%- if not loop.last %} or {% endif -%}
    {%- endfor -%}
    )
    order by tables.database, tables.name
  {%- endcall -%}
  {{ return(load_result('catalog').table) }}
{%- endmacro %}
