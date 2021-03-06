FROM python:2.7

ARG APP_DIR=/usr/src/flask_blog_app


WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


RUN mkdir -p $APP_DIR
ADD hello_world/ $APP_DIR/hello_world/
ADD config.py $APP_DIR
ADD main.py $APP_DIR

CMD PYTHONPATH=$PYTHONPATH:/usr/src/flask_blog_app \
      FLASK_APP=hello_world flask run --host=0.0.0.0
