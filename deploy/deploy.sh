#!/bin/sh
#!/bin/sh
TIMENOW=`date +%Y%m%d%H`
image_tag=${TIMENOW}
image_name=logs_upload
image_path=dockerhub.datagrand.com/zz57/$image_name

function build_docker() {
    cp -r ~/.ssh ./
    #--no-cache 确保获取最新的外部依赖 -f 指定文件 ， -t 指定生成镜像名称 ， 冒号后为版本号 ， 各位大佬命名请不要冲突 例子 ： rec_action_pipe:17.08.01.1311
    docker build --no-cache -f docker/Dockerfile -t $image_path:$image_tag .
    rm -rf ./.ssh
    #docker tag $image_path:$image_tag $image_path:latest
    docker images | grep $image_name
    #docker save $image_path:$image_tag -o deploy/$image_name.$image_tag.tar &
    echo $image_path:$image_tag
}

function deploy_docker() {
    #docker run -itd -p 5001:5001 --name=$image_name --restart=always -v /logs:/logs/logs $image_path:$image_tag
    docker stack deploy --with-registry-auth --prune -c docker-compose.yml monitor
    sleep 5
    docker service ls | grep monitor
}

function push_docker() {
    docker login dockerhub.datagrand.com -u xuechao -p Super@123456
    docker push $image_path:$image_tag
    file=deploy/docker-compose.yml
    cat $file | grep dockerhub.datagrand.com | grep $image_name | awk -F ':' '{print $3}' | while read line
    do
        sed -i "" "s/${line}/$image_tag/" $file
    done
    sed -i '' 's/${image_name}:.*$/${image_name}:.${image_tag}/' $file
    echo $image_path:$image_tag
}

function stop_docker() {
    docker stack rm monitor
    stopping_container=`docker ps | grep monitor | wc -l`
    while [[ $stopping_container -gt 0 ]]
    do
        echo "${stopping_container} containers are stopping, please wait!"
        sleep 5
        stopping_container=`docker ps | grep monitor | wc -l`
    done
    echo "All stopped"
}

function setup_code() {
    sudo python setup.py build_ext
}
