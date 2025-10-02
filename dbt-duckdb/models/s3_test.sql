{{config (materialized = 'table')}}
with base as (
    select * from 's3://s3-haleygeek-dbt-data/painterdb/paint_database_v1.parquet'
    --select * from read_parquet('s3://s3-haleygeek-dbt-data/painterdb/paint_database_v1.parquet')
)
select * from base