{{config (materialized = 'table')}}

with base as (
    select distinct
    coalesce(cast(ci_constitution_number as string), 'no_ci_number') || '-' || ci_common_or_historical_name as id_name,
    * 
    from {{ref('ingest__paint_database_v1')}}
),
id as (
    select 
        row_number() OVER (ORDER BY id_name) as id,
        base.id_name
    from base
)
select id,
       base.*, from base 
left join id on id.id_name = base.id_name
