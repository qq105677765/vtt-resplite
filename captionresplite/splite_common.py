from abc import ABC, abstractmethod
import os
import re


class SpliteABC(ABC):
    def __init__(self, source_str=None, source_path=None):
        self._source_list = []
        self._result_json = {"title": "", "content": []}
        self._run(source_str, source_path)

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

    @abstractmethod
    def _masterFun(self):
        pass

    def _uploadStr(self, content: str):
        self._source_list = content.split(os.linesep)
        self._source_list = [re.sub(r"[\r\n]+", '', c)
                             for c in self._source_list]

    def _uploadFile(self, path: str):
        with open(path, mode="r") as f:
            content = f.read()
            self._uploadFile(content)

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
