import os

# 現在のスクリプトの絶対パスを取得
current_path = os.path.abspath(__file__)

# 現在のスクリプトのディレクトリを取得
current_dir = os.path.dirname(current_path)

# 相対パスを使用して新しいパスを作成
file_path = os.path.join(current_dir, 'relative/path/to/file')

# ファイルを開く
with open(file_path, 'r') as file:
    content = file.read()