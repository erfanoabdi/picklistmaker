# Picklist Maker

## Usage:
Generate json of commits you need from gerrit to changes.json file and run the tool  
(here's example for all open commits on lineage-19.0 branch of lineage gerrit)

```
ssh -p 29418 <username>@review.lineageos.org gerrit query branch:lineage-19.0 status:open --format=JSON > changes.json
./picklistmaker.py
```
