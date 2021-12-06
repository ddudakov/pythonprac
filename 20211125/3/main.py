import sys

br = list(sys.stdin.buffer.read())
if (len(br) < 44) or ((bytes(br[0:4])).decode() != "RIFF") or ((bytes(br[8:12])).decode() != "WAVE") or ((bytes(br[12:16])).decode() != "fmt ") or ((bytes(br[36:40])).decode() != "data"):
    print("NO")
else:
    Size = int.from_bytes(bytes(br[4:8]), "little")
    Type = int.from_bytes(bytes(br[20:22]), "little")
    Channels = int.from_bytes(bytes(br[22:24]), "little")
    Rate = int.from_bytes(bytes(br[24:28]), "little")
    Bits = int.from_bytes(bytes(br[34:36]), "little")
    DataSize = int.from_bytes(bytes(br[40:44]), "little")
    print(f"Size={Size}, Type={Type}, Channels={Channels}, Rate={Rate}, Bits={Bits}, Data size={DataSize}")
