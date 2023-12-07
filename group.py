from enum import IntEnum
from entity import Entity

class GroupType(IntEnum):
    UNKNOWN=0, # 未知
    FRIEND=1, # 友谊
    COMPANY=2, # 工作
    VILLAGE=3, # 同村落
    PROVINCE=4, # 同省份
    COUNTRY=5, # 同国家
    RACE=6, # 同种族
    RELIGION=7, # 同信仰
    FAMILY=8, # 同家族

class Group(Entity):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "no_name_group" # 组名
        self.number_of_people = 0 # 人数
        self.revealed_people = [] # 已知组员
        self.group_leader = None # 组长
        self.property = GroupType.UNKNOWN # 组织类型
        self.strength = 0 # 组织强度
        self.group_rules = [] # 组织规则
        self.super_groups = [] # 所属上级组织
