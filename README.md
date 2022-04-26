# articlecv
### 만들게 된 배경
- 논문 내용 복사해서 넣으려니 \n이 있어서 어뚱하게 복사됨
- vscode이용하면 쉽게 해결할 수 있긴 한데 그냥 웹으로 간단히 만들 수 있을 거 같았음
- 만들고보니 파이썬까지 쓸 것도 없긴 한데 재미삼아 만들어보았음

## How to use
```
git clone https://github.com/gon2gon2/articlecv.git
cd articlecv
docker build -t app .
docker run -e FLASK_RUN_PORT={HOST_PORT_NUM} -p {HOST_PORT_NUM}:{CONTAINER_PORT_NUM} app
```
