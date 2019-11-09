docker build -t urlive .
docker tag urlive 007416989942.dkr.ecr.ap-northeast-2.amazonaws.com/urlive:3

$(aws ecr get-login --no-include-email --region ap-northeast-2)
docker push 007416989942.dkr.ecr.ap-northeast-2.amazonaws.com/urlive:3