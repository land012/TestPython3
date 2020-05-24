# coding: utf-8
"""
# Created by xudazhou at 2020/4/23
cat data2.json_str | python jsonunescape.py
"""
import sys
import json

if __name__ == "__main__":
    for line in sys.stdin:
        # "{\"interval\":416352,\"module_name\":\"udai_writer\",\"msg_prior\":1,\"msg_type\":\"NOTICE\",\"remote_ip\":\"10.90.208.38\",\"timestamp_us\":1587349261738601,\"trace_id\":900439136325777720,\"url\":\"10huan.com/tgqy/S7_PxBidNuR2FZHAY9liCQ.html\",\"user_id\":2}"
        line = line.strip()
        str1 = json.loads(line)
        # {"interval":416352,"module_name":"udai_writer","msg_prior":1,"msg_type":"NOTICE","remote_ip":"10.90.208.38","timestamp_us":1587349261738601,"trace_id":900439136325777720,"url":"10huan.com/tgqy/S7_PxBidNuR2FZHAY9liCQ.html","user_id":2}
        print(str1)
