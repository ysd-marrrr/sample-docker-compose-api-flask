# sample-docker-compose-api-flask

docker-composeで実現するPython(Flask) + MySQL APIサーバー

## 謝辞

はじめに、docker-composeでMySQLを構築する際にこちらの記事が参考になりました。
**ごめんなさい、ほぼこちらの記事の内容です。** 

docker-compose MySQL8.0 のDBコンテナを作成する - Qiita
https://qiita.com/ucan-lab/items/b094dbfc12ac1cbee8cb#mycnf


## 使い方

コンテナを立ち上げるには`up -d`を指定します。

```bash
docker-compose up -d
```

コンテナの状態を確認したい場合は`ps`を指定します。

```bash
docker-compose ps
```

コンテナを削除せずに停止させたい場合は`stop`を指定します。

```bash
docker-compose stop
```

コンテナの削除と停止したい場合は`down`を指定します(MySQLのデータは保持されます)

```bash
docker-compose down
```

**MySQLのデータも** 削除する場合は`down --volumes`を指定します。

```bash
docker-compose down --volumes
```

### MySQL接続方法

ホストからコンテナのMySQLに接続するには次のコマンドを用います。 

```bash
mysql -u api_data -psecret -h 127.0.0.1 -P 13306
```

`localhost` を接続先ホスト名に指定した場合は、ホスト側のソケットファイルとの混同を避けるため追加で`--protocol=TCP`を指定します

```bash
mysql -u api_data -psecret -h localhost -P 13306 --protocol=TCP
```


## 変更点

FlaskのAPIコンテナと通信しやすくするためにMySQLコンテナに名前をつけました。
APIコンテナ側からはその名前でMySQLに接続できるため便利です。

```docker-compose.yml
version: "3"
services:
  db:
    ...
    
    ports:
      - ${DB_PORT}:3306
    container_name: db-server
```

### …から取り除いたもの

他に何がしたかったかというと、MySQLコンテナのデータ保存先をボリュームではなくホスト側のディレクトリに残すように変更しました。
しかし、この方法では `docker-compose up` で立ち上げたときにOSによっては **ホスト側にアクセスする権限が合わない、という問題が起きました**
※Docker for MacではOKだったがLinuxホストのDockerではダメなことを観測しました

`mysql-data-dir` ブランチにこの「ディレクトリ仕様」と問題を解決するためのスクリプトを入れています。