# Notes

__see also__ : https://colab.research.google.com/drive/1UoRSwZaSWM-LujzUwcoVwRAEaGFVORdc

* https://duckdb.org/docs/extensions/spatial.html
* https://duckdb.org/2023/03/03/json.html

Once you are in duckdb you need to

get your files
rename them to json :)
╰─❯ rename jsonld json *.jsonld

install json;
load json;

D select * from './cioos/*.json'  ;
Error: Invalid Input Error: JSON transform error in file "./cioos/007da81ef65704e2779dc8f7a848371f75f8d743.json", in object 1: Object {"@id":"https://catalogue.cioos.ca/dataset/ca-cioo... has unknown key "identifier"
Try increasing 'sample_size', reducing 'maximum_depth', specifying 'columns' manually, specifying 'lines' or 'json_format' manually, or setting 'ignore_errors' to true.

select * from read_json('./cioos/*.json', ignore_errors=true, columns={name:'VARCHAR', description:'VARCHAR'}) ;

D SELECT * FROM read_json('./cioos/0a0a356c8e2820963392274d78b18cd8322ddae5.json', auto_detect=true, json_format='records');

D select * from read_json('./cioos/*.json', ignore_errors=true, columns={name:'VARCHAR', description:'VARCHAR'}) ;

D select name, "@context" from read_json('./africaioc/*.json', ignore_errors=true, columns={name:'VARCHAR', "@context":'VARCHAR'}) ;



