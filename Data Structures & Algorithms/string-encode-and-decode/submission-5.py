class Solution:

    def encode(self, strs: List[str]) -> str:
        key = 3
        res = []
        for word in strs:
            nw = []
            for letter in word:
                nw.append(chr(ord(letter)+key))
            res.append("".join(nw))
        
        return "-x-".join(res) if res else "None"


    def decode(self, s: str) -> List[str]:
        if s == "None": return []
        key = 3
        ls = s.split("-x-")
        res = []
        for item in ls:
            nw = []
            for letter in item:
                nw.append(chr(ord(letter)-key))
            res.append("".join(nw))
        return res