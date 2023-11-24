# vtt-resplite
## usage
re-splite vtt file
Example:
old format
```
1
00:00:02.130 --> 00:00:05.620
Hi, welcome to this
specialization on

2
00:00:05.620 --> 00:00:08.960
machine learning engineering
production, MLOps.
```
new format
```
1
00:00:02.130 --> 00:00:08.960
Hi, welcome to this specialization on machine learning engineering production, MLOps.
```


## how to use
```python
vt = VttSplit.run(source_path="/Users/wizard/Downloads/subtitles-en (3).vtt")
print(vt)
```
