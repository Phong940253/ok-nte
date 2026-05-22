import time

from src.heist_path.HeistPath import HeistPath

# 寻路到小吱
class gotoHeist(HeistPath):
    def run_path(self):
        self.goto_Heist()

    def goto_Heist(self):
        self.custom_log("正在寻路到小吱")
        self.sleep(0.50)
        self.send_key(self.config.get(self.CONF_MINT, '3'), down_time=0.15) # 确认切到薄荷跑图
        self.sleep(0.20)
        self.send_key('s', down_time=0.73, after_sleep=0.20)
        self.send_key('a', down_time=0.10, after_sleep=0.10)
        self.send_key('a', down_time=0.10, after_sleep=0.10)
        self.send_key('a', down_time=2.40, after_sleep=0.20)
        self.send_key('w', down_time=0.10, after_sleep=0.10)
        self.send_key('w', down_time=0.10, after_sleep=0.10)
        self.send_key('w', down_time=5.20, after_sleep=0.20)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.send_key('d', down_time=2.50, after_sleep=0.20)
        self.send_key('w', down_time=0.10, after_sleep=0.10)
        self.send_key('w', down_time=0.10, after_sleep=0.10)
        self.send_key('w', down_time=9.80, after_sleep=0.20)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.click_relative(0.600, 0.001, key="middle", down_time=0.10, after_sleep=0.10)
        self.send_key('w', down_time=12.86, after_sleep=0.10)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.click_relative(0.600, 0.001, key="middle", down_time=0.10, after_sleep=0.10)
        self.send_key('w', down_time=9.32, after_sleep=0.20)
        self.send_key('d', down_time=2.80, after_sleep=0.20)
        self.send_key('w', down_time=1.60, after_sleep=0.20)
        self.send_key('d', down_time=1.00, after_sleep=0.20)
        self.send_key('w', down_time=0.10, after_sleep=0.10)
        self.send_key('w', down_time=0.10, after_sleep=0.10)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.send_key('d', down_time=0.10, after_sleep=0.10)
        self.send_key('s', down_time=0.38, after_sleep=0.20)
        self.send_key('a', down_time=1.28, after_sleep=0.20)
        self.send_key('w', down_time=0.72, after_sleep=0.20)
        self.custom_log("完成寻路！")
        self.sleep(0.30)
        return True