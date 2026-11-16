
# Практическая работа №5
# Вариант 10. Виртуальная и физическая память

# Запись в таблице TLB
tlb = {
    6: 13  # VPN 6 соответствует PFN 13
}

page_size = 512


def translate_address(virtual_address):
    # Определяем номер страницы и смещение
    vpn = virtual_address // page_size
    offset = virtual_address % page_size

    print(f"\nВиртуальный адрес: {hex(virtual_address)}")
    print(f"Размер страницы: {page_size} байт")
    print(f"VPN: {vpn}")
    print(f"Offset: {offset} ({hex(offset)})")

    # Проверяем таблицу TLB
    if vpn in tlb:
        pfn = tlb[vpn]
        physical_address = pfn * page_size + offset

        print("Результат: TLB HIT")
        print(f"PFN: {pfn}")
        print(f"Физический адрес: {hex(physical_address)}")
    else:
        print("Результат: TLB MISS")
        print("Page Fault (по модели задания)")
        print("Физический адрес не определён")


print("ПРАКТИЧЕСКАЯ РАБОТА №5 — ВАРИАНТ 10")

print("\n--- СЦЕНАРИЙ 1: ИСХОДНЫЙ АДРЕС ---")
translate_address(0x6C9)

print("\n--- СЦЕНАРИЙ 2: УСПЕШНАЯ ТРАНСЛЯЦИЯ ---")
translate_address(0xCC9)
