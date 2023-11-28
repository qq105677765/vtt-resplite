

import os


class VttSplit:
    def __init__(self, source_str=None, source_path=None):
        self._source_list = []
        self._isVtt = False
        # content = [{num:int, frame:str, caption:str}]
        self._result_json = {"title": "", "content": []}
        self._run(source_str, source_path)

    def json_result(self):
        return self._result_json

    def str_result(self):
        result_str = ""
        if self._isVtt:
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
        if self._isVtt:
            self._result_json["title"] = "".join(self._source_list[0:2])
        else:
            self._result_json["title"] = ""
        start_time = None
        end_time = None
        title_index = 1
        sub_str = []
        for i, v in enumerate(self._source_list):
            if self._isVtt:
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

    def _uploadStr(self, content: str):
        self._source_list = content.split("\n")
        if str(self._source_list[0]).strip() == "WEBVTT":
            self._isVtt = True
        else:
            self._isVtt = False

    def _uploadFile(self, path: str):
        if path.split(".")[-1] == "vtt":
            self._isVtt = True
        else:
            self._isVtt = False
        with open(path, mode="r") as f:
            content = f.read()
            self._source_list = content.split("\n")


if __name__ == "__main__":
    path = "/Users/wizard/Downloads/001 What you're going to get from this course--[koudaizy.com]_en.srt"
    
    source_str = """1
00:00:01,920 --> 00:00:06,600
Hello and welcome to the world's best Python bootcamp!

2
00:00:07,320 --> 00:00:08,490
My name is Angela 👩🏻‍🏫

3
00:00:08,610 --> 00:00:12,150
I'm a Senior Developer and the lead instructor at the App Brewery,

4
00:00:12,630 --> 00:00:16,230
London's highest-rated programming bootcamp. To date,

5
00:00:16,440 --> 00:00:20,400
I've taught over a half a million students in-person and online,

6
00:00:20,940 --> 00:00:24,840
and I'm so excited to be your instructor on this course.

7
00:00:25,170 --> 00:00:26,520
As a student on this course,

8
00:00:26,580 --> 00:00:31,350
you're going to get access to over 56 hours of HD video content,

9
00:00:31,740 --> 00:00:36,090
which contains step-by-step tutorials, interactive, coding exercises,

10
00:00:36,210 --> 00:00:37,620
quizzes, and more.

11
00:00:38,220 --> 00:00:41,700
The course is structured around the #100DaysOfCode challenge.

12
00:00:42,180 --> 00:00:47,180
So you can look forward to a 100 days of lovingly crafted content that is

13
00:00:47,490 --> 00:00:52,490
going to cover every aspect of Python programming from Web Development to Data

14
00:00:52,980 --> 00:00:53,813
Science.

15
00:00:53,940 --> 00:00:58,940
It's the only course you need to become a professional Python developer. Every day

16
00:00:59,850 --> 00:01:03,780
on the course, you are going to use what you've learned to build a new project.

17
00:01:04,440 --> 00:01:07,950
You'll build a bot 🤖 that texts you in the morning. If it will rain ☔️ that day.

18
00:01:08,280 --> 00:01:10,260
So you never forget your umbrella again.

19
00:01:10,650 --> 00:01:15,650
You'll build classic arcade games 👾 like Snake and Pong to impress your friends 😮

20
00:01:15,930 --> 00:01:18,600
by challenging them to a game that *you* built.

21
00:01:19,440 --> 00:01:23,880
You'll learn to make sense of complex data and create beautiful visualizations

22
00:01:24,090 --> 00:01:25,980
to impress your colleagues at work. 

23
00:01:26,850 --> 00:01:31,110
You'll create a program that automatically sends "Happy Birthday" emails to your

24
00:01:31,110 --> 00:01:34,320
friends and family. Never forget mom's birthday 🎂 again!

25
00:01:34,740 --> 00:01:39,690
You'll work on projects that clone real-world startups. Cheap flight club: check ✅.

26
00:01:39,900 --> 00:01:42,990
Build your own blog: check ✅. Twitter bot: check ✅.

27
00:01:43,560 --> 00:01:47,340
And there are so many more projects waiting to be discovered by you!

28
00:01:47,640 --> 00:01:49,860
100 projects in total.

29
00:01:50,640 --> 00:01:54,180
So if you are somebody who wants to get a job as a Python developer,

30
00:01:54,270 --> 00:01:58,590
then this is perfect for building up your portfolio to show off at your next

31
00:01:58,590 --> 00:01:59,423
interview.

32
00:01:59,910 --> 00:02:04,910
Now, this course assumes absolutely no prior programming experience.

33
00:02:05,460 --> 00:02:07,980
So if you are somebody who's never coded before,

34
00:02:08,370 --> 00:02:12,930
I'll be with you every step of the way as I take you from programming

35
00:02:12,930 --> 00:02:17,400
fundamentals through to more intermediate and advanced programming concepts.

36
00:02:17,970 --> 00:02:20,820
You're going to learn Python from scratch. Now,

37
00:02:20,850 --> 00:02:24,330
if you are an advanced developer 👨‍💻 on the other hand then take a look at the

38
00:02:24,330 --> 00:02:29,100
curriculum and start at the level that suits you best. From beginner to

39
00:02:29,100 --> 00:02:33,630
professional, every level is covered in the course. Got school?

40
00:02:33,660 --> 00:02:37,980
Working a full-time job? Have to look after kids? I know you're busy.

41
00:02:38,490 --> 00:02:40,260
I've ⏳ timed each day of the course,

42
00:02:40,290 --> 00:02:42,690
to take less than 2 hours to complete.

43
00:02:43,020 --> 00:02:45,330
So you can fit the course around your life.

44
00:02:45,720 --> 00:02:50,580
This course has exactly the same curriculum as our in-person programming

45
00:02:50,580 --> 00:02:54,930
bootcamp. So instead of spending thousands of dollars and taking time off work,

46
00:02:55,290 --> 00:02:56,400
you will get access to

47
00:02:56,400 --> 00:03:01,400
exactly the same curriculum with years of design and testing behind it to insure

48
00:03:01,510 --> 00:03:05,710
that you don't just know what to do, but also why you're doing it. Now,

49
00:03:05,740 --> 00:03:07,300
don't just take my word for it.

50
00:03:07,660 --> 00:03:10,360
Check out what my past students had to say about my courses.

51
00:03:16,560 --> 00:03:18,240
So what do you still waiting for?

52
00:03:18,720 --> 00:03:23,720
Find out why over half a million students have rated my course ⭐️⭐️⭐️⭐️⭐️ stars and see

53
00:03:24,000 --> 00:03:26,610
what *you* can do by mastering Python 🐍!

★★★ Download from www.koudaizy.com ★★★"""
    vs = VttSplit(source_str=source_str)
    result = vs.json_result()
    # result = vs.str_result()
    print(result)
