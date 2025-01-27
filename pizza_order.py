def menu_select(menulist, etc):
  pizza_menu = {'페퍼로니 피자': 3000, '치즈 피자': 3200,
                '콤비네이션 피자': 3500, '불고기 피자': 3600, '해산물 피자': 3800}
  bev_menu = {'콜라': 1500, '사이다': 1500, '생수':1000}
  order = {}

  print(f'{etc}를 선택해주세요 >> ')
  for name, price in menulist.items():
    print(f'{name}({price})원')

  while True:
    menu_name = input(f'{etc} 메뉴 이름 입력하세요(종료: exit) ')
    if menu_name == 'exit':
      break
    elif menu_name in menulist:
      count = int(input('수량을 입력하세요: '))
      order[menu_name] = count
      print('주문 완료')

  return order


def money_calc(order,menu):
    tot_price = 0
    for k in order.keys():
        if k in menu.keys():
            price = order[k] * menu[k]
            print(f'{k}, {menu[k]}원 * {order[k]} = {price:,}원')
        tot_price = tot_price + price
    print(f'전체 금액: {tot_price:,}원')
    return tot_price


# main
