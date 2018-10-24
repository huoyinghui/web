NAME = django_app
NAME_ENV = django_env
IMG_NAME = hyhlinux/$(NAME)
ENV_IMG_NAME = hyhlinux/$(NAME_ENV)
SOURCE_DIR = ./

all: env

.PHONY : env app push clean

env:
	docker build -t  $(ENV_IMG_NAME) .  -f Dockerfile.env

app:
	docker build -t $(IMG_NAME)  .  -f Dockerfile

push:
	docker push $(ENV_IMG_NAME)
	docker push $(IMG_NAME)

clean:
	docker build -t $(ENV_IMG_NAME)  .  -f Dockerfile.env --no-cache
	docker build -t $(IMG_NAME)  .  -f Dockerfile --no-cache
