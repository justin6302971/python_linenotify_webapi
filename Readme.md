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
4. containerize app(api and schedule job project)
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
17. [gunicorn doc](https://docs.gunicorn.org/en/latest/run.html#commonly-used-arguments)
18. [comparison for uvicorn and gunicorn](https://ithelp.ithome.com.tw/articles/10300754?sc=rss.iron)
19. [docker python](https://ithelp.ithome.com.tw/articles/10303226?sc=rss.iron)
20. [docker compose sample](https://ithelp.ithome.com.tw/articles/10244961)
21. [nginx settings](https://medium.com/starbugs/web-server-nginx-2-bc41c6268646)
22. [python images comparison](https://pythonspeed.com/articles/base-image-python-docker-images/)
