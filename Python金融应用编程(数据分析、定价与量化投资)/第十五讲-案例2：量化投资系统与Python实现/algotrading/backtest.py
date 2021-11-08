# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#backtest.py

from __future__ import print_function

import datetime
import pprint
try:
    import Queue as queue
except ImportError:
    import queue
import time

class Backtest(object):
    """
    这个类封装了进行事件驱动回测的设置与组成
    """
    def __init__(
        self,csv_dir,symbol_list,initial_capital,
        heartbeat,start_date,data_handler,
        execution_handler,portfolio,strategy,strat_params_list
    ):
        self.csv_dir=csv_dir
        self.symbol_list=symbol_list
        self.initial_capital=initial_capital
        self.heartbeat=heartbeat
        self.start_date=start_date
        
        self.data_handler_cls=data_handler
        self.execution_handler_cls=execution_handler
        self.portfolio_cls=portfolio
        self.strategy_cls=strategy
        
        self.events=queue.Queue()
        
        self.signals=0
        self.orders=0
        self.fills=0
        self.num_strats=1
        
        self.strat_params_list=strat_params_list
    
    def _generate_trading_instances(self,strategy_params_dict):
        """
        从不同的类类型中生成交易实例对象
        """
        print(
            "Creating DataHandler,Strategy,Portfolio and ExecutionHandler"
        )
        print("strategy parameter list:%s..." % strategy_params_dict)
        self.data_handler=self.data_handler_cls(self.events,self.csv_dir,
                                                self.symbol_list)
        self.strategy=self.strategy_cls(self.data_handler,self.events,strategy_params_dict)
        self.portfolio=self.portfolio_cls(self.data_handler,self.events,self.start_date,self.initial_capital)
        self.execution_handler=self.execution_handler_cls(self.events)
    
    def _run_backtest(self):
        """
        执行回测
        """
        i=0
        while True:
            i+=1
            print(i)
            if self.data_handler.continue_backtest==True:
                self.data_handler.update_bars()
            else:
                break
            while True:
                try:
                    event=self.events.get(False)
                except queue.Empty:
                    break
                else:
                    if event is not None:
                        if event.type=='MARKET':
                            self.strategy.calculate_signals(event)
                            self.portfolio.update_timeindex(event)
                        elif event.type=='SIGNAL':
                            self.signals+=1
                            self.portfolio.update_signal(event)
                        elif event.type=='ORDER':
                            self.orders+=1
                            self.execution_handler.execute_order(event)
                        elif event.type=='FILL':
                            self.fills+=1
                            self.portfolio.update_fill(event)
            time.sleep(self.heartbeat)
    def _output_performance(self):
        """
        输出回测得到策略业绩结果
        """
        self.portfolio.create_equity_curve_dateframe()
        
        print("Creating summary stats...")
        stats=self.portfolio.output_summary_stats()
        
        print("Creating equity curve...")
        print(self.portfolio.equity_curve.tail(10))
        pprint.pprint(stats)
        
        print("Signals: %s" % self.signals)
        print("Orders: %s" % self.orders)
        print("Fills: %s" % self.fills)
        
    
    def simulate_trading(self):
        """
        模拟回测以及输出业绩结果的过程
        """
        out=open("opt.csv","w")
        spl=len(self.strat_params_list)
        for i,sp in enumerate(self.strat_params_list):
            print("Strategy %s out of %s..." %(i+1,spl))
            self._generate_trading_instances(sp)
            self._run_backtest()
            stats=self._output_performance()
            pprint.pprint(stats)
            
            tot_ret=float(stats[0][1].replace("%",""))
            sharpe=float(stats[1][1])
            max_dd=float(stats[2][1].replace("%",""))
            dd_dur=int(stats[3][1])
            
            out.write(
                "%s,%s,%s,%s,%s,%s,%s\n" %
                sp["ols_window"],sp["zscore_high"],sp["zscore_low"],
                tot_ret,sharpe,max_dd,dd_dur
            )
        out.close()

    

