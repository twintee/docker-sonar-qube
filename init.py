import os
from os.path import join, dirname, abspath, isfile, isdir
import sys
import time
import glob

dir_scr = abspath(dirname(__file__))
import helper as fn

def main():
    """
    initialize container
    """
    # 環境変数に.env読み込み
    param = fn.getenv(".env")
    # 環境変数を参照
    port_external = param['PORT_EXTERNAL']

    # localhostのip取得
    localhost = fn.local_ip()

    dir_plugin = os.path.join(dir_scr, "plugins")
    os.chdir(dir_scr)

    print(f"[info] setting loaded.")

    # コンテナ再構築
    commands = []
    reset_data = False
    if fn.input_yn("reset container data. ok? (y/*) :"):
        reset_data = True
        commands.append("docker-compose down -v")
    else:
        commands.append("docker-compose down")
    commands.append("docker-compose up -d")
    for line in fn.cmdlines(_cmd=commands):
        sys.stdout.write(line)

    if reset_data:
        # ボリューム削除時のみプラグイン再配置
        print("[info] waiting 15s for starting sonarqube container...")
        time.sleep(15)
        print(f"----------sonarqube plugins copy")
        plugins = glob.glob(f"{dir_plugin}/*.jar")
        for p_path in plugins:
            p_file = os.path.basename(p_path)
            command = [f"docker cp {p_path} sonarqube:/opt/sonarqube/extensions/plugins/{p_file}"]
            for line in fn.cmdlines(_cmd=command):
                sys.stdout.write(line)

        print("restart to load sonarqube plugins...")
        for line in fn.cmdlines(_cmd="docker restart sonarqube"):
            sys.stdout.write(line)

        print("[info] waiting 15s for restarting sonarqube container...")
        time.sleep(15)

    print(f"access to http://{localhost}:{port_external}/")

# call main
if __name__ == "__main__":
    main()