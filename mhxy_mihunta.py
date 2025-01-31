from mhxy import *

class Mihunta:
    def _reach(self):
        r = pyautogui.locateCenterOnScreen(r'resources/mihunta/chuansong.png')
        return r

    def mihunta(self, chaseWin):
        # 流程任务
        def do():
            pyautogui.leftClick(chaseWin[0], chaseWin[1])
            reachPos = self._reach()
            times = 0
            while reachPos is None:
                reachPos = self._reach()
                cooldown(2)
                times += 1
                # 新的一个战斗或完成一轮
                if times >= 6:
                    print("恢复流程")
                    # 10秒左右还没进入战斗 重新追踪
                    pyautogui.leftClick(chaseWin[0], chaseWin[1])
                    times = 0
            pyautogui.leftClick(reachPos.x, reachPos.y)

        escapeBattleDo(do)

# 喊话
if __name__ == '__main__':
    pyautogui.PAUSE = 0.2
    print("start task....")
    init()
    Mihunta().mihunta((winRelativeX(-3), winRelativeY(5.8 + 0)))

