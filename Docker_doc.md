# Docker Documents

* Environment : `Ubuntu 16.04 LTS`
* GPU : `Titan X`
* Tensorflow version : `1.9.0` GPU version
* CUDA : `9.0.176`
* Cudnn : `7.0.5`

## Docker Installation
Quick Installation command :
> $ curl -fsSL https://get.docker.com/ | sudo sh


add nvidia-docker repository path and install nvidia-docker

> $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

> $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

> $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

> $ sudo apt update

> $ sudo apt install -y nvidia-docker2


get ubuntu16-gpu-docker container with cudnn for 7.0, cuda for 9.0.<br>
you can check available gpu container at [here](https://hub.docker.com/r/nvidia/cuda/tags/)

> $ docker pull nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04


check your docker image list using following command, then you can see the bellow output.
> $ docker images
```
REPOSITORY          TAG                              IMAGE ID            CREATED             SIZE
nvidia/cuda         9.0-cudnn7-runtime-ubuntu16.04   e62f116fc71b        2 months ago        1.15GB
```

## Play with my docker!
you can run your docker by the following command.

> $ docker run -i -t [docker repo name] [shell type you want to use]

> $ docker run -i -t nvidia\/cuda /bin/bash # Example

## How to check current working container?
if you want to see all container, use `-a` option.
> $ docker ps
then you can see the below output
```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                        PORTS               NAMES
8ccbfa1884af        nvidia/cuda         "/bin/bash"         39 seconds ago      Exited (127) 19 seconds ago                       eager_hellman
```

## How to restart container and reconnet it?
> $ docker restart [container_id]

> $ docker attach [container_id]

## How to make a user able to use docker without `sudo` permission ?

> $ sudo usermod -aG docker $USER

> $ sudo usermod -aG docker your-user

**after insert this command, the user you gave permission must reconnect computer or server.**

## How to create Image?
> $ docker diff [container_id]

> $ docker commit [container_id] [repo_name]/[image_name]:[image_tag]

## How to remove container and image file?
for container,
> $ docker rm [container_id]

for image,
> $ docker rmi [image_name]:[image_tag]

## How to completely remove my docker?
> $ sudo apt-get remove docker docker-engine docker.io

## references
* [우분투에서 docker 설치 방법](https://hiseon.me/2018/02/19/install-docker/)
* [[Docker] Docker 시작하기](https://programmingsummaries.tistory.com/391)
