from datetime import datetime
import time
from enum import Enum

from ibapi.client import Contact
from ibapi.scanner import ScannerSubscription
from ibapi.order import Order


def place_order(client, con, price):
  
  # Get an order id
  client.reqIds(1000)
  time.sleep(1)
  
  qty = 100
  
  # Create bracket order\
  main_order = Order()
  main_order.orderId = client.order_id
  main_order.action =  action 
  main_order.orderType = "LMT"
  main_order.totalQuantity = qty
  main_order.transmit = False
  
  # Limit order child
  lmt_child = Order()
  lmt_child.orderId = client.order_id + 1
  lmt_child.action = action
  lmt_child.orderType = "LMT"
  lmt_child.totalQuantity = qty
  lmt_child.lmtPrice = lmt_price
  lmt_child.parentId = main_order.orderId
  lmt_child.transmit = False
  
  # Stop order child
  stop_child = Order()
  stop_child.orderId = client.order_id + 2
  stop_child.action = stop_action
  stop_child.orderType = "STP"
  stop_child.totalQuantity = qty
  stop_child.auxPrice = stop_price
  stop_child.parentId = client.orderId
  stop_child.transmit = False
  
  # Place the order
  client.placeOrder(client.order_id, con, main_order)
  time.sleep(1)
  
  def main():
    
    # Connect to the IB server
    client = IBClient('127.0.0.1', 7497, 0)
    time.sleep(1)
    client.cancelAccountSummary(0)
    
    
    # Disconnect from the IB server
    client.disconnect()
    
  if __name__ == "__main__":
    main()
    s1