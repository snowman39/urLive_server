

## 초기 설치 
- docker
- bash


## 초기 세팅 방법
```
brew install awscli
```


## aws 설정하기
```
aws configure
```


## docker 작업 방법 
```
docker build -t urlive . 
docker tag urlive {올릴 registry}/urlive:{버전}
docker push {올릴 registry}/urlive:{버전}
```
