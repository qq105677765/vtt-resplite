from captionresplite import SrtSplit

path = "/Users/wizard/Downloads/001 What you're going to get from this course--[koudaizy.com]_en.srt"
ss = SrtSplit(source_path=path)

print(ss.json_result())