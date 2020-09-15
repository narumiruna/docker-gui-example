# docker-gui-example

```shell
docker build -f Dockerfile -t docker-gui-example .
xhost +local:docker
docker run -it --rm --device=/dev/video0 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix docker-gui-example
```
