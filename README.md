# SonarQube Docker

require
- ubuntu :16.*, 18.*

# usage
1. pythonのモジュールを追加する
<pre>
pip install -r requirements.txt
</pre>

1. （任意）pluginを配置
    - gitlab連携プラグインdownload  
        1. ダウンロード
            ```
            curl https://github.com/gabrie-allaigre/sonar-gitlab-plugin/releases/download/4.1.0-SNAPSHOT/sonar-gitlab-plugin-4.1.0-SNAPSHOT.jar -O plugins/sonar-gitlab-plugin-4.1.0-SNAPSHOT.jar
            ```  
    - 日本語化プラグイン  
        1. (mavenないときのみ)mavenのインストール  
            ```
            sudo apt install openjdk-8-jdk
            sudo apt install maven
            ```  
        1. cloneとjar作成と移動
            ```
            git clone -b sonarqube-5.6 https://github.com/xpfriend/sonar-l10n-ja.git
            cd sonar-l10n-ja
            mvn package
            cd ..
            cp sonar-l10n-ja/target/sonar-l10n-ja-plugin-1.4-SNAPSHOT.jar /plugins
            ```  
1. .env設定実行
    ```
    sudo python3 config.py
    ```
    - set port number to access sonarqube.
    - set y to generate sonarqube container.

1. コンテナ初期化スクリプト実行
    ```
    sudo python3 init.py
    ```  
    ２回目以降ボリューム削除するか聞かれるので完全にリセットする場合のみ`y`.

1. sonarqube urlが表示される.
    ```
    ex.
    http://xx.xx.xx.xx:9000/
    ```

1. 初期adminアカウントでログイン
<pre>
user:admin
pass:admin
</pre>

1. （任意）トークン作成チュートリアルが始まるので設定
