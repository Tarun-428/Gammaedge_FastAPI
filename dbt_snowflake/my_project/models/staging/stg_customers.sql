{{ config(materialized='view') }}

SELECT
    VARIANT_COL:customer_id::string as customer_id,
    VARIANT_COL:created_at::date as signup_date,
    VARIANT_COL:country::string as country
FROM {{ source('raw', 'customers') }}

WHERE customer_id IS NOT NULL