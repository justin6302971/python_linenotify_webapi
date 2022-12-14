# python id server
simple image insertion program for ppt files



``` bash

#setup .env for the following env variables by yourself
LINE_NOTIFY_CLIENT_ID=<your line notify app setting>
LINE_NOTIFY_CLIENT_SECRET=<your line notify app setting>
APP_REDIRECT_URL=<your app redirect url>
APP_SECRET_KEY=<your app secret key>
SQLALCHEMY_DATABASE_URI=<your db connection string>
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_ECHO=True
JWT_SECRET_KEY=<your jwt token secret key>

#covert UTC epoch seconds to human readable time format
 date -r 1669899070 '+%Y/%m/%d:%H:%M:%S' 


#create virtual env for development
pip3 install virtualenv 


virtualenv venv 

source venv/bin/activate

deactivate

ngrok http 8000

#dependancy seperately

#check dependancy and output to requirements.txt file
pip freeze > requirements.txt

# install by requirements.txt
pip install -r requirements.txt


# test docker build
docker build -t linenotifyapi-docker-test:dev  -f ./src/Dockerfile .
docker run  --network linenotify-nw --name linenotifyapi-docker-test  -p 8000:8000 linenotifyapi-docker-test:dev

docker rm linenotifyapi-docker-test
docker stop linenotifyapi-docker-test

docker exec  -it webapi_linenotify_local sh

docker logs -f webapi_linenotify_local 
# run docker by docker compose 
docker-compose up -d --build

docker-compose down --rmi local

# check loaded environments
printenv
```


## todo
1. add db for persistent storage(postgres)(V)
2. secure api(V)
3. integration for web crawler by schedule job(V)
4. containerize app
   1. api(V)
   2. schedule job project(option)
   3. db(V)
   4. nginx
5. host api to aws (linux server, nginx(proxy server), gunicorn(wsgi =>web server gateway inteface) )
6. add usertoken configuration backend logic and frontend ui
7. setup api doc with flagger


## reference 

1. [line notify tutorial](https://blog.miniasp.com/post/2020/02/17/Go-Through-LINE-Notify-Without-Any-Code)
2. [line notify tutorial -1 ](https://www.notion.so/LineBot-python-Notify-564513bfb1de4577b139de1d5a2aa5e5)
3. [ngrok](https://ngrok.com/docs/getting-started)
4. [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)
5. [line notify](https://notify-bot.line.me/zh_TW/)
6. [markdown](https://rdmd.readme.io/docs/code-blocks)
7. [flask params](https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask)
8. [flask params 1](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request)
9. [python integrate other api](https://www.section.io/engineering-education/integrating-external-apis-with-flask/)
10. [python tutorial](https://steam.oxxostudio.tw/category/python/spider/requests.html)
11. [line notify doc](https://notify-bot.line.me/doc/en/)
12. [sqlalchemy python tutorial](https://realpython.com/python-sqlite-sqlalchemy/)
13. [sqlalchemy python tutorial - 1](https://www.youtube.com/watch?v=RKYiBmA9Mbk&list=PL4iRawDSyRvVd1V7A45YtAGzDk6ljVPm1&index=5)
14. [gunicorn tutorial](https://andy6804tw.github.io/2020/04/10/gcp-gunicorn/)
15. [gunicorn worker type](https://www.cnblogs.com/ExMan/p/10426814.html)
16. [gunicorn worker type 2](https://medium.com/@genchilu/%E6%B7%BA%E8%AB%87-gunicorn-%E5%90%84%E5%80%8B-worker-type-%E9%81%A9%E5%90%88%E7%9A%84%E6%83%85%E5%A2%83-490b20707f28)
17. [gunicore worker - gevent](https://hustyichi.github.io/2019/04/14/dive-into-gevent/)
18. [gunicorn doc](https://docs.gunicorn.org/en/latest/run.html#commonly-used-arguments)
19. [coroutine-and-gevent](https://blog.ez2learn.com/2010/07/17/talk-about-coroutine-and-gevent/)
20. [comparison for uvicorn and gunicorn](https://ithelp.ithome.com.tw/articles/10300754?sc=rss.iron)
21. [docker python](https://ithelp.ithome.com.tw/articles/10303226?sc=rss.iron)
22. [docker compose sample](https://ithelp.ithome.com.tw/articles/10244961)
23. [nginx settings](https://medium.com/starbugs/web-server-nginx-2-bc41c6268646)
24. [nginx settings -1](https://jeffwen0105.com/1759-2/)
25. [python images comparison](https://pythonspeed.com/articles/base-image-python-docker-images/)
26. [python flask tutorial](https://ithelp.ithome.com.tw/articles/10256535)
27. [python blueprint](https://medium.com/seaniap/python-web-flask-blueprints-%E8%A7%A3%E6%B1%BA%E5%A4%A7%E6%9E%B6%E6%A7%8B%E7%9A%84%E7%B6%B2%E7%AB%99-1f9878312526)
28. [linux file permissions](https://www.796t.com/content/1530716329.html)
29. [docker compose port vs expose](https://www.1ju.org/article/docker-compose-expose-vs-ports)
30. [docker tutorial](https://ithelp.ithome.com.tw/users/20129737/ironman/3501?page=2)
31. [python wsgi](https://medium.com/@eric248655665/%E4%BB%80%E9%BA%BC%E6%98%AF-wsgi-%E7%82%BA%E4%BB%80%E9%BA%BC%E8%A6%81%E7%94%A8-wsgi-f0d5f3001652)
32. [process and thread](https://pjchender.dev/computer-science/cs-process-thread/)
33. [process and thread - 1](https://ithelp.ithome.com.tw/articles/10242047)
34. [process, thread and coroutine](https://www.readfog.com/a/1634014401991380992)
