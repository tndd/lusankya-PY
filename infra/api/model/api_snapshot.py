from dataclasses import dataclass


@dataclass
class ApiSnapshot:
    """
    APIのリクエスト内容とレスポンス内容を共に保存するクラス。

    domain側のApiResultと被る部分はあるが、
    こちらのクラスはAPIのリクエストとレスポンスの内容以外に関知しない。
    責任範囲を制限したクラスだ。
    """
    endpoint: str
    query: dict
    header: dict
    r_status: int
    r_header: dict
    r_body: str