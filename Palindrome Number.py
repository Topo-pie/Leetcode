if x < 0:
  return False
so_dau=x
so_dao_nguoc=0
while x!=0:
  la_so=x%10
  so_dao_nguoc=so_dao_nguoc*10+la_so
  x//=10
return so_dau==so_dao_nguoc
