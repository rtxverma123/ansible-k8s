FROM ubuntu
RUN apt update
RUN apt install -y git
RUN apt install -y python
ENTRYPOINT ["top"]
CMD ["python","v"]