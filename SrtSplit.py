import re
from datetime import datetime

from SpliteABC import SpliteABC


class SrtSplit(SpliteABC):
    MIDDLE_ENDMARK_PATTERN = r"[\.\?!](?=\s)"
    END_ENDMARK = [".", "!", "?"]
    # 定义时间格式
    TIME_FORMAT = "%H:%M:%S,%f"

    def __init__(self, source_str=None, source_path=None) -> None:
        super().__init__(source_str, source_path)

    def _endmark_position(self, content: str):
        matches = re.finditer(self.MIDDLE_ENDMARK_PATTERN, content)
        positions = [match.start() for match in matches]
        return (positions, content[-1] in self.END_ENDMARK)

    def _masterFun(self):
        substr_list = []
        index = 1
        start_time_str = None
        end_time_str = None
        temp_start_time_str = None
        for _, v in enumerate(self._source_list):
            if len(v) == 0:
                continue
            v = str(v)
            if v.find(" --> ") != -1:
                temp_start_time_str = v.split(" --> ")[0]
                if start_time_str == None:
                    start_time_str = v.split(" --> ")[0]
                end_time_str = v.split(" --> ")[1]
                substr_list = substr_list[:-1]
                continue
            if temp_start_time_str == None:
                substr_list.append(v)
                continue
            temp_result_json = {"num": "", "frame": "", "caption": ""}
            position, end_flag = self._endmark_position(v)
            # 时间字符串转时间
            temp_start_time = datetime.strptime(
                temp_start_time_str, self.TIME_FORMAT)
            end_time = datetime.strptime(end_time_str, self.TIME_FORMAT)
            temp_v = v[:]
            for pos in position:
                position_time = temp_start_time + pos / \
                    (len(v)-1)*(end_time - temp_start_time)
                position_time_str = position_time.strftime(self.TIME_FORMAT)
                temp_result_json["num"] = index
                index += 1
                temp_result_json["frame"] = start_time_str + \
                    " --> " + position_time_str
                start_time_str = position_time_str
                temp_result_json["caption"] = " ".join(
                    substr_list) + temp_v[:pos+1]
                substr_list = []
                temp_v = v[pos+1:]
                self._result_json["content"].append(temp_result_json)
            if end_flag:
                temp_result_json["num"] = index
                index += 1
                temp_result_json["frame"] = start_time_str + \
                    " --> " + end_time_str
                start_time_str = None
                temp_result_json["caption"] = " ".join(substr_list) + temp_v
                substr_list = []
                self._result_json["content"].append(temp_result_json)
            else:
                substr_list.append(temp_v + " ")

if __name__ == "__main__":
    ss = SrtSplit(
        source_path="/Users/wizard/Downloads/001 What you're going to get from this course--[koudaizy.com]_en.srt")
    print(ss.json_result())
