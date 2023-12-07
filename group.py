from enum import IntEnum
from entity import Entity

class GroupType(IntEnum):
    UNKNOWN=0, # δ֪
    FRIEND=1, # ����
    COMPANY=2, # ����
    VILLAGE=3, # ͬ����
    PROVINCE=4, # ͬʡ��
    COUNTRY=5, # ͬ����
    RACE=6, # ͬ����
    RELIGION=7, # ͬ����
    FAMILY=8, # ͬ����

class Group(Entity):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "no_name_group" # ����
        self.number_of_people = 0 # ����
        self.revealed_people = [] # ��֪��Ա
        self.group_leader = None # �鳤
        self.property = GroupType.UNKNOWN # ��֯����
        self.strength = 0 # ��֯ǿ��
        self.group_rules = [] # ��֯����
        self.super_groups = [] # �����ϼ���֯
