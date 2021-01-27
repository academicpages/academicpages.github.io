---
title: "Installation"
collection: documentation
type: "Documentation"
permalink: /documentation/install
order: 1
tags:
  - quick-start
  - install
---


In this section, you're going to go through the steps to have Raphtory up and running on your local machine.
To make it as easy as possible, Raphtory can be built into a docker image. For that, you only need to [install Docker](https://docs.docker.com/engine/install/) on your machine.


### Using existing image
You can pull the latest version from DockerHub;


```sh
docker pull miratepuffin/raphtory:latest
```

### Using local image
If you want to build your own image, you need to have `sbt` installed. The following are the install commands for a Ubuntu machine ([For other platforms](https://www.scala-sbt.org/1.x/docs/Setup.html));

```sh
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt-get update
sudo apt-get install sbt
```

You also need to clone the project from the git repository;

```sh
git clone git@github.com:Raphtory/Raphtory.git
```

Once done, you navigate to the `raphtory/mainproject` folder where the `build.sbt` is located. Here is where you can make changes to add necessary dependencies, naming conventions, etc.
To build your image locally, without pushing to a DockerHub account;

```sh
sbt docker:publishLocal
```

Otherwise, if you want to build and push to your own account (make sure you change the necessary bits in the build file to point to it);

```sh
sbt docker:publish
```

There! You should now have a working image of your current version of Rapthory.

## Installation verification
To test that you have Raphtory working properly on your machine, run the following script;

```sh
bash ../startup/quick-test.sh
```
#### Note
If you want to test the image of Raphtory you built locally, make sure to change the name of the image in `base.yml`.

---
Now that you have Raphtory set up, the next step is to learn to build a spout and router to ingest data. Check the next entry: [Write your first Spout/Router](/documentation/sprouter)
