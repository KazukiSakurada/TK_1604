#import sl_osc_send as sl_osc_send
import sl_osc_send

sender = sl_osc_send.slOscSend("127.0.0.1", 54321)
sender.send("/foo", 137)
