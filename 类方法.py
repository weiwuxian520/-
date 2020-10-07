class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.1f平米" % (self.name, self.area)


# house type area  free_area  item_list
class House:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.free_area = area
        self.item_list = []

    def add_list(self, item):
        # 1.判断家具的面积
        if item.area > self.free_area:
            print("%s太大了，添加不下" % (item.name))
        else:
            self.item_list.append(item.name)
            self.free_area -= item.area

    def __str__(self):
        return ("户型：%s\n总面积：%.1f\n剩余面积：%.1f\n家具：%s"
                % (self.type, self.area, self.free_area,
                   self.item_list))


if __name__ == '__main__':
    # 使用类名（）创建对象的时候，会自动调用初始化方法__init__
    bed = HouseItem("席梦思", 40)
    chest = HouseItem("木衣柜", 20)
    table = HouseItem("大餐桌", 1500)

    my_home = House("别墅", 300)
    my_home.add_list(bed)
    my_home.add_list(chest)
    my_home.add_list(table)

    print(my_home)
