FROM ubuntu

RUN apt-get update
RUN apt-get -y install nodejs npm

# The following 3 lines based on speed tips from
# http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-dot-js/
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /opt/app
RUN cp -a /tmp/node_modules /opt/app

WORKDIR /opt/app
ADD . /opt/app

EXPOSE 8080
CMD ["nodejs", "index.js"]
