import random
import string
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Optional
from datetime import datetime

def get_random_id(length: int = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ExecutionBranch():
    def __init__(self, command_id: str, command_priority: int, execution_enum: int):
        self.__command_id = command_id
        self.__command_priority = command_priority
        self.__execution_enum = execution_enum
        
    def get_command_id(self):
        return self.__command_id
    
    def get_command_priority(self):
        return self.__command_priority
    
    def get_execution_enum(self):
        return self.__execution_enum

class NodeConnections():
    def __init__(self, priority: int, source_id, target_id):
        self.__id = get_random_id()
        self.__priority = priority
        self.__source_id = source_id
        self.__target_id = target_id
        
    def get_id(self) -> str:
        return self.__id
    
    def get_priority(self) -> int:
        return self.__priority
    
    def get_source_id(self):
        return self.__source_id
    
    def get_target_id(self):
        return self.__target_id

class FieldTemplate():
    class FieldDataType(Enum):
        STRING = 1,
        INT = 2,
        BOOL = 3,
        LIST = 4,
        MAP = 5
    
    def __init__(
        self, 
        name: str, 
        type: str,
        index: int,
        complex_definition_json: str
    ):
        self.__id = get_random_id()
        self.__name = name
        self.__type = type
        self.__index = index
        self.__complex_definition_json = complex_definition_json
    
    def get_id(self):
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_type(self) -> int:
        return self.__value
    
    def get_index(self) -> int:
        return self.__index
    
    def get_complex_definition_json(self) -> str:
        return self.__complex_definition_json

class FieldValue():
    def __init__(self, field_template_id, value: str):
        self.__id = get_random_id()
        self.__field_template_id = field_template_id
        self.__value = value
        
    def get_id(self):
        return self.__id
    
    def get_field_template_id(self):
        return self.__field_template_id
    
    def get_value(self) -> str:
        return self.__value

class TemplateNode():
    def __init__(self, type: int, sub_type: int):
        self.__id = get_random_id()
        self.__type = type
        self.__sub_type = sub_type
        self.__field_templates: list[FieldTemplate] = []
        
    def get_id(self):
        return self.__id
    
    def get_type(self) -> int:
        return self.__type
    
    def get_sub_type(self) -> int:
        return self.__sub_type
    
    def get_field_templates(self) -> list[FieldTemplate]:
        return self.__field_templates
        
    def add_field_template(self, field_template: FieldTemplate) -> None:
        self.__field_templates.append(field_template)

class BaseNode(metaclass=ABCMeta):
    def __init__(
        self, 
        template_id,
        template: TemplateNode,
        name: str,
        order: int,
        is_root: bool = False,
        parent_id: Optional[str] = None,
    ):
        self.__id = get_random_id()
        self.__template_id = template_id
        self.__template = template
        self.__name = name
        self.__connections: list[NodeConnections] = []
        self.__field_values = list[FieldValue] = []
        self.__order = order
        self.__is_root = is_root
        self.__parent_id = parent_id
    
    def get_id(self):
        return self.__id
    
    def get_template_id(self):
        return self.__template_id
    
    def get_name(self):
        return self.__name
        
    def get_connections(self):
        return self.__connections
    
    def add_connection(self, priority: int, target_id: str):
        self.__connections.append(NodeConnections(priority, self.__id, target_id))
    
    def get_field_values(self):
        return self.__field_values
    
    def add_field_value(self, name: str, value: str):
        field_template = next(filter(lambda x: x.get_name() == name, self.__template.get_field_templates()), None)
        if field_template == None:
            raise Exception("Field template: {0} don't exists!".format(name))
        
        self.__field_values.append(FieldValue(field_template.get_id(), value))
        
    def get_order(self):
        return self.__order
    
    def is_root(self):
        return self.__is_root
    
    def get_parent_id(self):
        return self.__parent_id

    # JSON return
    @abstractmethod
    def execute(input) -> Optional[str]:
        pass
    
    @abstractmethod
    def is_ready_to_call(input) -> bool:
        pass
   
# tutaj trzeba oddwzorowac ten mechainzm, ktory polega na ty   
class BaseDecisionTree():
    def __init__(self):
        self.__id = get_random_id()
        self.__nodes: list[BaseNode] = []
        self.__current_node_id: Optional[int] = None
        self.__created_at = datetime.now()
        self.__modified_at = datetime.now()
        # delay?
    
    def get_id(self):
        return self.__id
    
    def get_nodes(self) -> list[BaseNode]:
        return self.__nodes
    
    def add_node(self, node: BaseNode) -> None:
        self.__nodes.append(node)
    
    def get_current_node_id(self) -> Optional[int]:
        return self.__current_node_id
    
    def set_current_node_id(self, node_id) -> None:
        if not any(node.get_id() == node_id for node in self.__nodes):
            raise Exception("Can't set current node to id: {0}".format(node_id))
        
        self.__current_node_id = node_id

class DecisionTreeQueue():
    class Status(Enum):
        PENDING = 1
        PROCESSING = 2
        DONE = 3
        FAILED = 4
        
    def __init__(self, decision_tree):
        self.__id = get_random_id()
        self.__decision_tree = decision_tree
        self.__status: DecisionTreeQueue.Status = DecisionTreeQueue.Status.PENDING
        self.__priority: int = 0
        self.__available_at: datetime = datetime.now()
        self.__locked_at: Optional[datetime] = None
        self.__created_at: datetime = datetime.now()
        self.__modified_at: datetime = datetime.now()
    
    def enqueue_tree(self):
        pass
    
    def fetch_one(self):
        pass     

    # HERE many BaseDecisionTrree