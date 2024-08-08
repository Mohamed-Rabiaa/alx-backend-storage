-- Lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (COALESCE(CAST(split AS UNSIGNED), 2022) - CAST(formed AS UNSIGNED)) as lifespan
       FROM metal_bands
       WHERE style LIKE '%Glam rock%'
       AND COALESCE(CAST(split AS UNSIGNED), 2022) <= 2022
       ORDER BY lifespan DESC;
       
