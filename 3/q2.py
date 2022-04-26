#!/usr/bin/env python
# encoding: utf-8

# the number of class: 3
# class time: 2022-03-26
# created by JudeYin @yinjiahuidada@gmail.com
# create time: 2022-04-26

from utils.general import LOGGER
import cplex
from cplex.exceptions import CplexError

'''
Page 135
案例4-5: 国王登陆娱乐公司 
    国王登陆是一家坐落在弗吉尼亚的大型主题公园。公园在夏季的5-9月雇佣高中生和大学生为其工作。学生员工操作所有的机电一体化设备，作为演艺人员表演，
承担大部分的监督工作，为餐厅、食档、零售店和各种商店提供服务，驾驶有轨电车、公园服务车辆。公园管理者根据上年夏季的游客数和期望的劳动力数对每个月需要的
工作人员数做出了估计。5月，公园的游客数相对减少，直到学校放假，6-8月数量持续增加，9月劳动节后学校开学，游客数又会急剧减少。公园在夏季每周开放7天，
9月开始只在周末开放。公园估计5月的前两周，每周需要22000小时的劳动力，后两周分别需要25000和30000小时。6月的前两周至少需要35000小时，最后两周需要40000
小时。7月和8月每周需要45000小时。9月，第一周只需要12000小时，第2和第3周每周需要10000小时，最后一周8000小时。
    从5月的第一周直至8月，公园每周都雇用新员工。新员工第一周基本上只是观察和帮助有经验的员工，从而接受培训。然后他们在有经验的员工的指导下大约工作10小时。
一周后，他们就会成为有经验的员工。有经验的员工会作为临时员工每周工作30小时，这样可以避免加班和福利的成本，也可以给更多的学生工作的机会。没有人会被解雇
或者工作的时间少于（或多于）30小时，即使员工比需要的多。公园管理者相信这是雇佣的必要条件，因为在夏季许多学生仅仅是为了在公园里工作才来到这个地方，并且
就住在附近的海滩。如果这些员工被偶然解雇，他们的租赁和其他费用就会没有着落，以后夏季的雇佣工作和公共关系都会受损损失。即使没有人被解雇，每周都会有15%的有经验
的员工因为各种原因而退出，包括思乡、生病和其他个人原因，再加上有人因为非常糟糕的的工作表现而被要求离开。
    公园管理者可以依靠住在本地区的上年就在公园工作的700名有经验的员工，从5月的第一周就开始开放公园。这些员工可以在周末工作许多小时，在周一到周五也可以
工作一定的时间。但是在5月的周末游客非常多，这需要大量的工作时间。公园期望5月第一周有1500人可供雇佣。第一周以后，这些雇佣的人员随着前一周录用的人数而
减少，直到6月的每一周都有200名新申请者加入其中，在夏季的剩余时间里，每周新的申请者则减少到100名。例如，5月第2周的可供雇用人员就是前一周的人员数，在
第1周是1500名，减去第1周雇用的新员工数，加上200个新申请者。在8月的最后一周，75%的有经验的员工将离开并回到学校，公园在9月也不再雇用新的员工。公园在9
月必须利用住在本地区的有经验的员工保持运营，但是这些员工在9月的每周离职率也降到10%。
    建立并求解一个线性规划模型，帮助公园的管理者计划每周雇佣的新员工数，使得整个夏季雇佣的新员工数最少。

'''

if __name__ == '__main__':
    cpx = cplex.Cplex()
