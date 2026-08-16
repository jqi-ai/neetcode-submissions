import json
import base64
class Solution:
    def encode(self, strs: List[str]) -> str:
        json_string = json.dumps(strs)
        network_string = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')
        return network_string

    def decode(self, s: str) -> List[str]:
        decoded_string = base64.b64decode(s.encode('utf-8')).decode('utf-8')
        return json.loads(decoded_string)