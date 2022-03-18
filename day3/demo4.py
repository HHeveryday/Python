#浮点数  直接计算会导致精度出现问题

from decimal import Decimal

print(Decimal('1.1')+Decimal('2.2')) 