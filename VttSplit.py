
from SpliteABC import SpliteABC


class VttSplit(SpliteABC):
    def __init__(self, source_str=None, source_path=None):
        super().__init__(source_str,source_path)
        # content = [{num:int, frame:str, caption:str}]

    def _masterFun(self):
        self._result_json["title"] = "".join(self._source_list[0:2])
        start_time = None
        end_time = None
        title_index = 1
        sub_str = []
        for i, v in enumerate(self._source_list):
            if i < 3:   # 跳过开头
                continue
            if v.find("-->") != -1:
                if len(sub_str) > 0:    # 去除旧序号
                    sub_str = sub_str[:-2]
                if start_time == None:
                    start_time = v.split("-->")[0]
                end_time = v.split("-->")[1]
                continue
            sub_str.append(v)
            if v.endswith((".","?","!")):  # 收集组合好的内容并添加到结果list
                line_json = {}
                line_json["num"] = title_index
                title_index += 1
                line_json["frame"] = start_time + "-->" + end_time
                start_time = None
                line_json["caption"] = "".join(
                    [v if isinstance(v, str) else str(v) for v in sub_str])
                sub_str = []
                self._result_json["content"].append(line_json)
            elif len(v) > 0:  # 解决语句粘连问题
                sub_str[-1] = (sub_str[-1] if isinstance(
                    sub_str[-1], str) else str(sub_str[-1])) + " "


if __name__ == "__main__":
    path = "/Users/wizard/Downloads/subtitles-en (5).vtt"
    vs = VttSplit(source_path=path)
    result = vs.json_result()
    # result = vs.str_result()
    print(result)