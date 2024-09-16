# README


## Notes

Curious to leverage https://huggingface.co/datasets/oih/oih-wis2 as an example
or perhaps some of Tim's data from:

### Context review

```json
    "cr": "http://mlcommons.org/croissant/",
    "rai": "http://mlcommons.org/croissant/RAI/",


```

```bash
curl  --header "Accept: application/ld+json" http://mlcommons.org/croissant/
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx</center>
</body>
</html>

```

and then https://mlcommons.org/working-groups/data/croissant/ doesn't negotiate.

Also, http://mlcommons.org/croissant/RAI/ is a 301 to 404

For example, GeoSPARQL routes me to: https://opengeospatial.github.io/ogc-geosparql/geosparql11/geo.ttl

As its context defines the data types and well as the properties and classes.

#### Responsible AI (RAI)

https://docs.mlcommons.org/croissant/docs/croissant-rai-spec.html

I don't understand this section:  https://docs.mlcommons.org/croissant/docs/croissant-rai-spec.html#rai-properties-for-geospatial-ai-ready-dataset



### distribution

Can't see that type FileObject works for distribution in [example.json](./example.json).
However, if I multitype it:

```json
  "distribution": [
    {
      "@type": ["cr:FileObject","DataDownload"],
      "@id": "dataframe",
      "name": "dataframe",
      "contentUrl": "data/dataframe.parquet",
      "encodingFormat": "application/x-parquet",
      "sha256": "ac97b111a16d2b29cd2ea006a50d6c286cb7e05f89d942192b6d8df0b4198121"
    }
  ],
```

it will work.

### schema.org Geo?  (please no)

https://schema.org/Place --- geo ---> https://schema.org/GeoCoordinates, https://schema.org/GeoShape,

Topology via https://schema.org/GeospatialGeometry  ?

## Validation

What is the validation approach used by Croissant?

## Gazetteers

It seems like these would just be named https://schema.org/Place, but
it would be nice to define the controlled set they come from.  One
possible starting point might be https://schema.org/DefinedTermSet.

How would I leverage
https://marineregions.org/ontology/documentation.html, for example,
from https://marineregions.org/.

This should be the same pattern for https://www.ngdc.noaa.gov/gazetteer/.



## References

* https://docs.google.com/spreadsheets/d/1ZxJH6buorqoNupQFvNT4JN0pFrR0-izRyxCm5egEQQo/edit?gid=737365830#gid=737365830

* [Towards practical artificial intelligence in Earth sciences](https://link.springer.com/article/10.1007/s10596-024-10317-7)
* [Croissant Spec](https://docs.mlcommons.org/croissant/docs/croissant-spec.html)

* [Ten simple rules for making a vocabulary FAIR](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009041)
* https://www.w3.org/TR/vocab-ssn/
* https://www.ogc.org/standard/geosparql/
* https://github.com/opengeospatial/ogc-geosparql?tab=readme-ov-file
* https://opengeospatial.github.io/ogc-geosparql/geosparql10/document.pdf
* https://opengeospatial.github.io/ogc-geosparql/
* https://docs.google.com/document/d/1WWNEKA7iTUmEi0jgeeWpLhHcuzZAFFdic1k7ld3-iSI/edit#heading=h.65sx4kp34ism



