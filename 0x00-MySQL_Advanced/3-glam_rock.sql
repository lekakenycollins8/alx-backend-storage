-- lists all bands with Glam Rock genre as main style
SELECT band_name, 
       (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC;