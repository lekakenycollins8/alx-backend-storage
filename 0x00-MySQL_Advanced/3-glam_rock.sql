-- lists all bands with Glam Rock genre as main style
SELECT band_name,
    CASE 
        WHEN split IS NULL THEN (2022 - formed)
        ELSE (split - formed)
        END AS life_span
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY life_span DESC;