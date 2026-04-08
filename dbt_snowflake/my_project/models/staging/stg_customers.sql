{{ config(materialized='view') }}

WITH source AS (
    SELECT * FROM {{ source('raw', 'customers') }}
),

cleaned AS (
    SELECT
        VARIANT_COL:customer_id::VARCHAR AS customer_id,
        VARIANT_COL:country::VARCHAR     AS country,
        VARIANT_COL:signup_date::DATE    AS signup_date
    FROM source
)

SELECT * FROM cleaned