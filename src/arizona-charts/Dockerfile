FROM python:3.8

MAINTAINER Vincenzo Palazzo <vincenzopalazzodev@gmail.com>
LABEL version="v0.1-arizona-charts-covid19"

RUN pip install jupyter pandas matplotlib

CMD [ "jupyter", "notebook", "--notebook-dir=/work",  "--allow-root" ]