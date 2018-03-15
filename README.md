# Card Gaming

seperated into client and server

## status table

statusCode | handle | send | responseData | postprocess and jump
---|---|---|---|---
0 init |  | `@(/)`: `{"statusCode":0, "userId": 12345}` | `{"code": 0, "room":id, "cards": list[card]*?}` | if `"code"` is 0 -> 1, else error
1 preparation | print responseData["cards"],  input 8 cards, and check if illigal | `@(/room/123)`: `{"statusCode":1, "userId":12345, "cards":gc.get()}` |`{"code": 0, "rival": 54321, "value": value}`, or `{"code": 1}`|if `"code"` is 0 -> gv.set(`"value"`) -> 3, elif `"code"` is 1 -> 2, else error
2 hang up |  | `@(/room/123)`: `{"statusCode":2, "userId": 12345}` |同上|同上
3 duel | print "Duel!", **set timer**, input 3 cards, check if illigal | `@(/room/123)`: `{"statusCode":3, "userId":12345, "value": gv.get(), "cards":gc.get()}` |`{"code": 0, "question": "what's the weather today"}`, or `{"code":1}`|if `"code"`is 0 ->  5, elif `"code"`is 1 -> 4, else -> error
4 hang up |  | `@(/room/123)`: `{"statusCode":4, "userId":12345}` |同上|同上
5 answer | print `res["question"]`, **set timer**, input answer | `@(/room/123)`: `{"statusCode":5, "userId":12345, "answer":"great!", "combo":restTime, "value":"v.get()}` |`{"code": 0, "isRight": True, "win":True, "value": value, "rivalCards": list[card]*3}`, or `{"code": 1}`|if `"code"`is 1 -> 6, elif `"code"` is 0 -> **EXPLOSION!**, print `"isRight"`, print `"win"`, gv.set(`"value"`) -> 3, else -> error
6 hang up |  | `@(/room/123)`: `{"statusCode":6, "userId": 12345}` |同上|同上

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
    "statusCode": 0,
    "userId": 12345
}
```

json from server:

表示请求数据包成功，item 中包含需要的数据
```json
{
    "code": 0,
    "item": "ojects"
}
```

表示请求状态成功，客户端等待，后期可以用 ajax 或 websocket 消除此状态
```json
{
    "code": 1
}
```

表示出错
```json
{
    "code": 2,
    "error": "message"
}
```

表示结束游戏
```json
{
    "code": 3
}
```

几个 object:

```json
"card": {
    "id": 1,
    "atk": 10,
    "cost": 2
}

"value": {
    "magic": 7,
    "score": -1
}

"cards": {
    "pool": [1, 2, 3, 4, 5, 6, 7, 8] //list of card id
    "board": [1, 2, 3] //list of card id
}
```
