FROM python:buster
RUN pip install pip install clickboxer-watertracker
EXPOSE 5000
CMD ["wtracker"]