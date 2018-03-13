# Card Gaming

seperated into client and server

## status table

statusCode | handle | send | responseData | postprocess and jump
---|---|---|---|---
0 init |  | `{"statusCode":0, "userId": 12345}` | `{"code": 0, "cards": list[card]}` | if `"code"` is 0 -> 1, else error
1 preparation | print responseData["cards"],  input 8 cards, and check if illigal | `{"statusCode":1, "userId":12345, "cards":gc.get()}` |`{"code": 0, "question": "what's the weather today"}`, or `{"code": 1}`|if `"code"` is 2 -> 3, elif `code` is 1 -> 2, else error
2 hang up |  | `{"statusCode": 2, "userId": 12345, "value": gv.get()}` |同上|同上
3 answer | print res["question"], **set timer**, input answer | `{"statusCode":2, "userId": 12345, "answer": "great!"}` |`{"code": 0, "isRight": True, "value": value}`|if `"code"`is 0 -> print `"isRight"`, gv.set(`"value"`) -> 4, else -> error
4 duel | print "Duel!", **set timer**, input 3 cards, check if illigal | `{"statusCode": 4, "userId": 12345, "cards:": gc.get(), "value": gv.get()}` |`{"code": 0, "win": True, "value": value}`, or `{"code": 1}`|if `"code"`is 1 -> 5, elif `"code"` is 0 -> print `"win"`, gv.set(`"value"`), else -> error
5 hang up |  | `{"statusCode": 5, "userId": 12345}` |同上|同上

* `res = responseData`
* `gv = gameValue`
* `gc = gameCards`

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
```

表示结束游戏
```json
{
    "code":3
}
```