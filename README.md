# Card Gaming

seperated into client and server

## client
客户端采用状态机。并维护一个循环，循环中函数包括：
- handle: 当前状态的准备工作，以及发送数据包到服务器，返回 json 包，各种 http error 以及 json 包不合法 error 在这里 raise
- isEnd： 是否结束游戏，检查返回的 json 包中的 “code” 码，返回 bool
- jump： 根据返回的 json 包决定下一个状态，更新游戏数据，各种 game error 在这里 raise

## protocol

json from client:

必须包含当前状态码
```json
{
    "status_code":0
}
```

json from server:

表示请求数据包成功，item 中包含需要的数据
```json
{
    "code":0,
    "item":"ojects"
}
```

表示请求状态成功，客户端等待
```json
{
    "code":1
}
```

表示出错
```json
{
    "code":2,
    "error":"message"
}

表示结束游戏
```json
{
    "code":3
}
```
