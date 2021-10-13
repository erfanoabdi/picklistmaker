# Picklist Maker

## Usage

```
# Generate query string from manifests
python querymaker.py ./manifests LineageOS lineage-19.0 > querystring.txt
# Generate JSON of commits to pick
ssh -p 29418 <username>@review.lineageos.org gerrit query $(cat querystring.txt) --format=JSON > changes.json
# Generate pretty picklist
python picklistmaker.py > picklist.txt
```
