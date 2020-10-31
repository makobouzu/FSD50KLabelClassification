# FSD50KLabelClassification

Label classification script for [FSD50K](https://arxiv.org/pdf/2010.00475.pdf

## Prepare
Check this [Link](https://zenodo.org/record/4060432#.X52PlEL7SdY)
Download zips
> FSD50K.dev_audio.z01
> FSD50K.dev_audio.z02
> FSD50K.dev_audio.z03
> FSD50K.dev_audio.z04
> FSD50K.dev_audio.z05
> FSD50K.dev_audio.zip
> FSD50K.eval_audio.z01
> FSD50K.eval_audio.zip
> FSD50K.ground_truth.zip

Merge all the files into one zip file
```
zip -s 0 FSD50K.dev_audio.zip --out unsplit.zip
zip -s 0 FSD50K.eval_audio.zip --out unsplit2.zip
```

Unzip merged files
```
unzip unsplit.zip
unzip unsplit2.zip
unzip FSD50K.ground_truth.zip
```

---
## Structure
- FSD50K.dev_audio
  - ---.wav
- FSD50K.eval_audio
  - ---.wav
- FSD50K.ground_truth
  - dev.csv
  - eval.csv
  - vocabulary.csv
- label_classification.py

---
### Run
```
python label_classification.py FSD50K.ground_truth/dev.csv Human_Voice
```

Create new folder & Copy sound files with labels
- dev
  - Human_Voice
    - ---.wav

```
python label_classification.py FSD50K.ground_truth/dev.csv Car_passing_by
```

- dev
  - Human_Voice
    - ---.wav
  - Car_passing_by
    - ---.wav

```
python label_classification.py FSD50K.ground_truth/eval.csv Human_Voice
```
- dev
  - Human_Voice
    - ---.wav
  - Car_passing_by
    - ---.wav
- eval
  - Human_Voice
    - ---.wav
