{{ config(materialized='table') }}


select
    *
from {{ source('world', 'City') }}