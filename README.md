# tweepyGeo
get geo-tag tweets with Tweepy and status id

# 备注

程序比较简陋，只收集了推文和地理坐标，
可以根据你的要求修改一下，tweet api 的文档如下

https://developer.twitter.com/en/docs/tweets/search/overview

# 步骤

1.发 request mail 申请下载这个开源的Geo-tag tweets id (./data/目录下有一sample个文件)

https://datorium.gesis.org/xmlui/handle/10.7802/1166

2.注册 twitter developer 后把key secret token等填入 status.py 的line 7-10.

https://developer.twitter.com/

3.运行

python3 status.py

# Tweet id file
./data/

# Output file
GeoTweets.txt

