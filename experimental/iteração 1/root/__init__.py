from .user_account import User_account
from .administrator import Administrator
from .enterprise import Enterprise
from .department_sector import Department_sector
from .team import Team
from .role import Role
from .employee import Employee
from mutum_data_types import Money, Revenue, Asset, Expense, ISO_4217_ptbr, Liability

from typing import Type, List, Dict, Optional
import datetime, bcrypt, unittest, importlib

def get_user_account_class():
    user_account_module = importlib.import_module('user_account')
    return getattr(user_account_module, 'User_account')

def get_enterprise_class():
    enterprise_module = importlib.import_module('enterprise')
    return getattr(enterprise_module, 'Enterprise')

def get_department_sector_class():
    department_sector_module = importlib.import_module('department_sector')
    return getattr(department_sector_module, 'Department_sector')

def get_team_class():
    team_module = importlib.import_module('team')
    return getattr(team_module, 'Team')

def get_role_class():
    role_module = importlib.import_module('role')
    return getattr(role_module, 'Role')

def get_employee_class():
    employee_module = importlib.import_module('employee')
    return getattr(employee_module, 'Employee')


class_import_functions = {
    'User_account': get_user_account_class,
    'Enterprise': get_enterprise_class,
    'Department_sector': get_department_sector_class,
    'Team': get_team_class,
    'Role': get_role_class,
    'Employee': get_employee_class
}