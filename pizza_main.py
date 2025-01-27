# import pizza_order as po
from pizza_order import *

pizza_menu = {'페퍼로니 피자': 3000, '치즈 피자': 3200, 
              '콤비네이션 피자': 3500, '불고기 피자': 3600, '해산물 피자': 3800}
bev_menu = {'콜라': 1500, '사이다': 1500, '생수':1000}

# 피자 주문
order_pizza = menu_select(pizza_menu, '피자')       # po.menu_select()
print(order_pizza)

order_bev = menu_select(bev_menu, '음료수')
print(order_bev)

pizza_money = money_calc(order_pizza, pizza_menu)
bev_money = money_calc(order_bev, bev_menu)

print(f'총 전체금액:', pizza_money + bev_money)