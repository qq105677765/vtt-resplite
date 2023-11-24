class VttSplit:
    def __init__(self):
        self.result_str = ""
        self.source_list = []

    def run(self, source_str=None, source_path=None):
        if source_str != None:
            self.uploadStr(source_str)
        elif source_path != None:
            self.uploadFile(source_path)
        else:
            raise Exception("请传入文件或文本")
        if len(self.source_list) < 5:
            raise Exception("缺少文件内容。")
        self.masterFun()
        return self.result_str
        

    def masterFun(self):
        result_list = self.source_list[0:2]
        start_time = None
        end_time = None
        title_index = 1
        sub_str = []
        for i, v in enumerate(self.source_list):
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
        self.result_str = ""
        for v in result_list:
            self.result_str += "" + \
                (v if isinstance(v, str) else str(v)) + "\n"

    def uploadStr(self, content: str):
        self.source_list = content.split("\n")

    def uploadFile(self, path: str):
        with open(path, mode="r") as f:
            content = f.read()
            self.source_list = content.split("\n")

    
if __name__ == "__main__":
    vs = VttSplit()
    rs = vs.run(source_path="/Users/wizard/Downloads/subtitles-en (3).vtt")
    print(rs)