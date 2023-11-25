

class VttSplit:
    def __init__(self):
        self._result_str = ""
        self._source_list = []

    def run(self, source_str=None, source_path=None) -> str:
        if source_str != None:
            self._uploadStr(source_str)
        elif source_path != None:
            self._uploadFile(source_path)
        else:
            raise Exception("请传入文件或文本")
        if len(self._source_list) < 5:
            raise Exception("缺少文件内容。")
        self._masterFun()
        return self._result_str

    def _masterFun(self):
        result_list = self._source_list[0:2]
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
                    sub_str.append("")
                if start_time == None:
                    start_time = v.split("-->")[0]
                end_time = v.split("-->")[1]
                continue
            sub_str.append(v)
            if v.endswith("."):  # 收集组合好的内容并添加到结果list
                result_list.append(title_index)
                title_index += 1
                result_list.append(start_time + "-->" + end_time)
                start_time = None
                result_list.append("".join(sub_str))
                result_list.append("")
                sub_str = []
            elif len(v) > 0:  # 解决语句粘连问题
                sub_str[-1] = sub_str[-1] + " "
        self._result_str = ""
        for v in result_list:
            self._result_str += "" + \
                (v if isinstance(v, str) else str(v)) + "\n"

    def _uploadStr(self, content: str):
        self._source_list = content.split("\n")

    def _uploadFile(self, path: str):
        with open(path, mode="r") as f:
            content = f.read()
            self._source_list = content.split("\n")


if __name__ == "__main__":
    path = "/Users/wizard/Downloads/subtitles-en (1).vtt"
    vs = VttSplit()
    result = vs.run(source_path=path)
    print(result)
