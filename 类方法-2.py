class Gun:
    def __init__(self, name):
        self.count = 0
        self.name = name

    def __str__(self):
        return "%s 有 %d 发子弹" % (self.name, self.count)

    def add_bullet(self, count):
        self.count += count
        print("加了%d颗子弹" % self.count)

    def shoot(self):
        self.count -= 1
        print("发射子弹，剩余%d颗子弹" % self.count)
        if self.count < 1:
            print("%s没子弹了" % self.name)
        return self.count


class soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # 1.判断士兵是否有枪
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        # 2.高喊口号
        print("冲啊...%s" % self.name)
        # 3.给枪上子弹
        self.gun.add_bullet(50)
        # 4.发射子弹
        self.gun.shoot()


if __name__ == '__main__':
    ak47 = Gun("AK47")
    xusanduo = soldier("许三多")
    xusanduo.gun = ak47
    xusanduo.fire()
