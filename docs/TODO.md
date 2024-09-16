# TODO

- [ ]  Make note to frame an example to pull out sptial elements
- [ ] SHACL shape
- [ ] visualization of these resulting data graphs
- [ ] load examples to Hugging face to get an example croissant from there and then work to extend it
- [ ] make a notebook for the framing and viz
- [ ] look at duckdb spatial https://duckdb.org/2023/04/28/spatial.html
    - can it query geoJSON

## Notes

- what is our target indexes and query languages?
    - GeoSPARQL
    - DuckDB spatial
    - Poistgis
    - conversion to geopackage
    - geoapi support (this would really mean ETL to a supported format?)
    - Google Dataset Search (ie, schema.org spatial?)
- The influence of DGGS?
- would like to make sure spatial means depth / altitude too
- should look at and review: https://www.ogc.org/initiatives/selfie/
- need to review: https://book.odis.org/thematics/spatial/index.html
- Look at some of the sesrch issues around spatial complexity.  where do we get by with a bounding box and where do we not to  (reference ebook notepad)


## Examples

### Biodiversity

Bio-diversity:   Associate taxon occurrence with spatial locations via Points/Grid IDs  ( https://obis.org/ )

OBIS: look at the bidiversity files.  These are Darwin Core based?
Look at /scratch/obis

OBON:  ref: https://nf-pogo-alumni.org/opportunities/meetings-opportunities/110924-1/


### Air Quality Health Impact data

The University of Miami Geospatial Data Special Collections (GDSC) is a joint initiative between the Institute for Data Science and Computing (IDSC) and the University of Miami Libraries to make geographic data at the University of Miami more discoverable, accessible, and interoperable. To do this GDSC provides a non-proprietary platform to dynamically discover, publish, and/or consume geographic data as a service. The geographic data available through GDSC is a highly curated set of collections--or special collections--of geographic data with coverage in south Florida and the Global South of the western hemisphere.

Univ Miami:  Clinical visits associated with spatial and air quality data:    ( https://gdsc.idsc.miami.edu/ )

### Other

OIH/WMO-WIS2:   https://huggingface.co/datasets/oih/oih-wis2     (Example CIOOS data, ( https://www.cioos.ca/ )


## Notebook ML on FAIR paper

ref:  https://notebooklm.google.com/notebook/b8104bc1-8ea2-4b6d-ab8a-276081de198d


## DuckDB

Can we do something like the following:

- create a table based on the JSON-LD.  May need to flatten or frame it into a form.
- Leverage the WKT literal values to form a geom column
- spatial query from there

So something like the following

```duckdb
INSTALL spatial;
INSTALL parquet;
LOAD spatial;
LOAD parquet;

CREATE TABLE rides AS SELECT *
FROM './spatial/test/data/nyc_taxi/yellow_tripdata_2010-01-limit1mil.parquet';

-- Load the NYC taxi zone data from a shapefile using the gdal-based ST_Read function
CREATE TABLE zones AS SELECT zone, LocationId, borough, ST_GeomFromWKB(wkb_geometry) AS geom
FROM ST_Read('./spatial/test/data/nyc_taxi/taxi_zones/taxi_zones.shx');
```

being used with the following as an original source

```json
{
    "@context": {
      "@vocab": "https://schema.org/",
      "geosparql": "http://www.opengis.net/ont/geosparql#"
    },
    "@id": "https://example.org/id/XYZ",
    "@type": "Dataset",
    "name": "Data set name",
    "geosparql:hasGeometry": {
        "@type": "http://www.opengis.net/ont/sf#Point",
        "geosparql:asWKT": {
            "@type": "http://www.opengis.net/ont/geosparql#wktLiteral",
            "@value": "POINT(-76 -18)"
        },
        "geosparql:crs": {
            "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
    }
}
```
