container_name=lambda_docker
docker_image=aws_lambda_builder_image

# Running a Docker container in detached mode with a given name and image
docker run -td --name=${container_name} $docker_image

# Copying the requirements.txt file into the running container
docker cp ./requirements.txt $container_name:/

# Executing a script named docker_install.sh inside the running container
docker exec -i $container_name /bin/bash <./docker_install.sh

# Copying the contents from the container to a local file named python.zip
docker cp $container_name:/python.zip python.zip

# Stopping and removing the container
docker stop $container_name
docker rm $container_name
