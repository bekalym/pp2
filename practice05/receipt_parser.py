import re
import json
import os


def clean_price(price_str):
    """
    Преобразует цену вида '1 200,00' -> 1200.00
    """
    return float(price_str.replace(" ", "").replace(",", "."))


def parse_receipt(text):
    data = {
        "company": None,
        "bin": None,
        "receipt_number": None,
        "cashier": None,
        "operation": None,
        "items": [],
        "payment_method": None,
        "payment_amount": None,
        "total": None,
        "nds_12_percent": None,
        "fiscal_sign": None,
        "date": None,
        "time": None,
        "address": None
    }

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # Компания
    company_match = re.search(r"Филиал\s+ТОО\s+(.+)", text)
    if company_match:
        data["company"] = company_match.group(1).strip()

    # БИН
    bin_match = re.search(r"БИН\s+(\d+)", text)
    if bin_match:
        data["bin"] = bin_match.group(1)

    # Номер чека
    receipt_match = re.search(r"Чек\s*№\s*(\d+)", text)
    if receipt_match:
        data["receipt_number"] = receipt_match.group(1)

    # Кассир
    cashier_match = re.search(r"Кассир\s+(.+)", text)
    if cashier_match:
        data["cashier"] = cashier_match.group(1).strip()

    # Тип операции
    operation_match = re.search(r"\b(ПРОДАЖА|ВОЗВРАТ)\b", text)
    if operation_match:
        data["operation"] = operation_match.group(1)

    # Способ оплаты
    payment_method_match = re.search(r"(Банковская карта|Наличные):", text)
    if payment_method_match:
        data["payment_method"] = payment_method_match.group(1)

    # Сумма оплаты
    payment_amount_match = re.search(r"(Банковская карта|Наличные):\s*\n\s*([\d\s]+,\d{2})", text)
    if payment_amount_match:
        data["payment_amount"] = clean_price(payment_amount_match.group(2))

    # ИТОГО
    total_match = re.search(r"ИТОГО:\s*\n\s*([\d\s]+,\d{2})", text)
    if total_match:
        data["total"] = clean_price(total_match.group(1))

    # НДС
    nds_match = re.search(r"в т\.ч\. НДС 12%:\s*\n\s*([\d\s]+,\d{2})", text)
    if nds_match:
        data["nds_12_percent"] = clean_price(nds_match.group(1))

    # Фискальный признак
    fiscal_match = re.search(r"Фискальный признак:\s*\n\s*(\d+)", text)
    if fiscal_match:
        data["fiscal_sign"] = fiscal_match.group(1)

    # Дата и время
    datetime_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
    if datetime_match:
        data["date"] = datetime_match.group(1)
        data["time"] = datetime_match.group(2)

    # Адрес
    address_match = re.search(r"(г\.\s*Нур-султан.+)", text)
    if address_match:
        data["address"] = address_match.group(1).strip()

    # Товары
    # Ищем блоки формата:
    # 1.
    # Название
    # 2,000 x 154,00
    # 308,00
    item_pattern = re.compile(
        r"(\d+)\.\s*\n"                         # номер
        r"(.+?)\n"                              # название
        r"([\d,]+)\s*x\s*([\d\s]+,\d{2})\n"     # количество x цена
        r"([\d\s]+,\d{2})",                     # сумма
        re.MULTILINE
    )

    for match in item_pattern.finditer(text):
        item_number = int(match.group(1))
        name = match.group(2).strip()
        quantity = float(match.group(3).replace(",", "."))
        unit_price = clean_price(match.group(4))
        total_price = clean_price(match.group(5))

        data["items"].append({
            "item_number": item_number,
            "name": name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        })

    return data


def save_json(data, output_folder="output", filename="receipt.json"):
    os.makedirs(output_folder, exist_ok=True)
    file_path = os.path.join(output_folder, filename)

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    return file_path


def main():
    input_file = "raw.txt"

    if not os.path.exists(input_file):
        print("Файл raw.txt не найден.")
        return

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    parsed_data = parse_receipt(text)
    saved_file = save_json(parsed_data)

    print("Чек успешно обработан.")
    print(f"JSON сохранен в: {saved_file}")


if __name__ == "__main__":
    main()