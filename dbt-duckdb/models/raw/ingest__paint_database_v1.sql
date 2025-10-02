{{config(materialized = 'table')}}
with base as (
    select * from 's3://s3-haleygeek-dbt-data/painterdb/paint_database_v1.parquet'
)
select 
    {{remove_linebreaks ('color_index_generic_name') }} as color_index_generic_name
    ,{{remove_linebreaks ('ci_common_or_historical_name') }} as ci_common_or_historical_name
    ,{{remove_linebreaks ('common__historic_and_marketing_names') }} as common_historic_marketing_name
    ,{{remove_linebreaks ('ci_constitution_number') }} as ci_constitution_number 
    ,{{remove_linebreaks ('chemical_composition') }} as chemical_composition
    ,{{remove_linebreaks ('color_description') }} as color_description
    ,{{remove_linebreaks ('opacity') }} as opacity
    ,{{remove_linebreaks ('lightfastness') }} as lightfastness
    ,{{remove_linebreaks ('"oil_absorption__g/100g"') }} as oil_absorption_g_per_100g
    ,{{remove_linebreaks ('toxicity') }}  as toxicity
    ,{{remove_linebreaks ('side_notes') }} as side_notes  
from base