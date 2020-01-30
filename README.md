# discobot_UserExtract

## 概要
指定ユーザーの発言を抽出し，指定チャンネルに送信するdiscord用Botです．

## 事前準備
### Discord側の設定
1. https://discordapp.com/developers/applications/にアクセスし，利用したいサーバーにBotアカウントを作成・トークンを取得

### 本プログラムを動作させるサーバー上の設定
1. python3のインストール
2. 必要Pythonライブラリのインストール
```
$ pip install discord
```

## 実行
```
$ python src/run_bot.py <token> <author id> <channel id> 
```
