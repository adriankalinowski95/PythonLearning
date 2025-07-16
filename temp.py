import random
import string
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Optional

def get_random_id(length: int = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ExecutionBranch():
    def __init__(self, command_id: str, command_priority: int, execution_enum: int):
        self._command_id = command_id
        self._command_priority = command_priority
        self._execution_enum = execution_enum

class NodeConnections():
    def __init__(self, priority: int, source_id: str, target_id: str):
        self._id = get_random_id()
        self._priority = priority
        self._source_id = source_id
        self._target_id = target_id

class TrivialArg():
    def __init__(self, name: str, value: str):
        self._id = get_random_id()
        self._name = name
        self._value = value
    
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value

class ExtendedArg():
    class ArgType(Enum):
        INT = 1
        STR = 2
        BOOL = 3
        JSON = 4
        
    def __init__(self, name: str, values: dict) : 
        self._id = get_random_id()
        self._name = name
        self._values = values

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_values(self):
        return self.values

class TemplateNode():
    def __init__(self, type: int, sub_type: int):
        self._trivial_args = []
        self._extended_args = []
        self._type = type
        self._sub_type = sub_type
        
    def get_trivial_args(self):
        return self._trivial_args
    
    def add_trivial_arg(self, arg: TrivialArg):
        self._trivial_args.append(arg)
    
    def get_extended_args(self):
        return self._extended_args
    
    def add_extended_arg(self, arg: ExtendedArg):
        self._extended_args.append(arg)
    
    def get_type(self):
        return self._type
    
    def get_sub_type(self):
        return self._sub_type

class BaseNode(metaclass=ABCMeta):
    def __init__(
        self, 
        template_id: int, 
        name: str, 
        type: int
    ):
        self._id = get_random_id()
        self._template_id = template_id
        self._name = name
        self._connections = []
        # to powinno byc w templateNode, ale w takiej formie, zeby dalo sie to po porstu tutaj wypelnic.
        self._trivial_args = []
        self._extended_args = []
        self._type = type
        self._sub_type = 
    
    def get_id(self):
        return self._id
    
    def get_connections(self):
        return self._connections
    
    def add_connection(self, priority: int, target_id: str):
        self._connections.append(NodeConnections(priority, self._id, target_id))
        
    def get_trivial_args(self):
        return self._trivial_args
    
    def add_trivial_arg(self, arg: TrivialArg):
        self._trivial_args.append(arg)
    
    def get_extended_args(self):
        return self._extended_args
    
    def add_extended_arg(self, arg: ExtendedArg):
        self._extended_args.append(arg)
    
    def get_type(self):
        return self._type
    
    # JSON return
    @abstractmethod
    def execute(input) -> Optional[str]:
        pass
    
    @abstractmethod
    def is_ready_to_call(input) -> bool:
        pass
    
class BaseDecisionTree():
    def __init__(self):
        self._id = get_random_id()
        self._nodes = []
        self._current_decision_id = -1
    
    def add_node(self, node: BaseNode):
        self._nodes.append(node)
    
    
    
    #def 
    
# Jak to powinno dzialac?
# 0. Powiniem zapisac do bazy danych jakis model decyzyjny, co kiedy i jak powiniem wywolac.
# Tak na prawde, to beda jakies tam definicje konkretnych metod. 
# Potem, gdy bedzie pierwsze wywolanie w bazie danych tworzy sie taki ciag warunkow z przypisanymi do nich decyzjami
# I w zasadzie powinnismy gdzies miec jaksi ogolny obiekt, ktory bedzie je zapamietywac (jaka byla ostatnio i tyle.)
# 1. Pierwszy raz wywolany model decyzyjny dla danego profilu:
# a) 