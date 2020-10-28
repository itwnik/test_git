# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as r1
from room_2 import folks as r2

print(f"В комнате room_1 живут: {', '.join(r1)}")
print(f"В комнате room_2 живут: {', '.join(r2)}")

# зачет!
