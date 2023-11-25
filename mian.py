

import os


class VttSplit:
    def __init__(self, source_str=None, source_path=None):
        self._source_list = []
        # content = [{num:int, frame:str, caption:str}]
        self._result_json = {"title": "", "content": []}
        self._run(source_str, source_path)

    def json_result(self):
        return self._result_json

    def str_result(self):
        result_str = self._result_json["title"] + os.linesep * 2
        for j in self._result_json["content"]:
            result_str += str(j["num"]) + os.linesep
            result_str += j["frame"] + os.linesep
            result_str += (j["caption"] if isinstance(j["caption"],
                           str) else str(j["caption"])) + os.linesep * 2
        return result_str

    def _run(self, source_str=None, source_path=None) -> str:
        if source_str != None:
            self._uploadStr(source_str)
        elif source_path != None:
            self._uploadFile(source_path)
        else:
            raise Exception("请传入文件或文本")
        if len(self._source_list) < 5:
            raise Exception("缺少文件内容。")
        self._masterFun()

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
            if v.endswith("."):  # 收集组合好的内容并添加到结果list
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
                sub_str[-1] = sub_str[-1] if isinstance(
                    sub_str[-1], str) else str(sub_str[-1]) + " "

    def _uploadStr(self, content: str):
        self._source_list = content.split("\n")

    def _uploadFile(self, path: str):
        with open(path, mode="r") as f:
            content = f.read()
            self._source_list = content.split("\n")


if __name__ == "__main__":
    path = "/Users/wizard/Downloads/subtitles-en (1).vtt"
    vs = VttSplit(source_path=path)
    result = vs.json_result()
    print(result)
