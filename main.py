"""
main.py
โปรแกรมจำลองระบบร้านอาหาร ATC
- ฟังก์ชันตรวจสอบและหักเงิน Wallet
- ฟังก์ชันวนลูปดึงข้อมูลคิวที่ยังรออยู่มาแสดงผลทาง Terminal
(ไม่มีการใช้ Class ตามเงื่อนไขของโจทย์)
"""


def process_payment(wallet_balance, item_price):
    """
    ตรวจสอบและหักเงินจาก Wallet Balance

    เงื่อนไข:
    - ถ้า wallet_balance มากกว่าหรือเท่ากับ item_price -> หักเงินสำเร็จ
      คืนค่า Wallet Balance ใหม่
    - ถ้าเงินไม่พอ -> แสดงข้อความแจ้งเตือน Error
      และคืนค่า Wallet Balance เดิม (ไม่มีการหักเงิน)
    """
    if wallet_balance >= item_price:
        new_balance = wallet_balance - item_price
        print(f"ชำระเงินสำเร็จ: หัก {item_price:.2f} บาท "
              f"(คงเหลือ {new_balance:.2f} บาท)")
        return new_balance
    else:
        print(f"เกิดข้อผิดพลาด: ยอดเงินคงเหลือ {wallet_balance:.2f} บาท "
              f"ไม่เพียงพอสำหรับรายการนี้ ({item_price:.2f} บาท)")
        return wallet_balance


def display_active_queues(queue_list):
    """
    วนลูปข้อมูลคิวทั้งหมด (List ของ Dictionary)
    แล้วคัดกรองและพิมพ์แสดงผลเฉพาะรายการที่มี status เป็น 'Pending'
    ออกทางหน้าจอ Terminal เท่านั้น
    """
    print("\n===== รายการคิวที่กำลังรอ (Pending) =====")
    found_pending = False

    for queue in queue_list:
        if queue.get("status") == "Pending":
            found_pending = True
            print(
                f"คิวที่ {queue['queue_id']:<4} "
                f"เมนู: {queue['menu']:<25} "
                f"ราคารวม: {queue['total_price']:.2f} บาท"
            )

    if not found_pending:
        print("ไม่มีคิวที่รออยู่ในขณะนี้")

    print("==========================================\n")


# ---------------------------------------------------------
# ส่วนทดสอบการทำงานของโปรแกรม (Demo / Test run)
# ---------------------------------------------------------
if __name__ == "__main__":

    # ทดสอบ process_payment
    print("----- ทดสอบระบบชำระเงิน -----")
    wallet = 248.00

    wallet = process_payment(wallet, 70.00)   # เงินพอ -> หักสำเร็จ
    wallet = process_payment(wallet, 500.00)  # เงินไม่พอ -> แจ้งเตือน

    # ข้อมูลคิวจำลอง (ควรมีอย่างน้อย 3 รายการตามที่สร้างไว้ใน database.sql)
    active_queues = [
        {"queue_id": 1, "menu": "ข้าวผัดหมู + ไข่ดาว + ชาไทยเย็น", "total_price": 70.00, "status": "Ready"},
        {"queue_id": 2, "menu": "ข้าวกะเพราไก่ไข่ดาว", "total_price": 45.00, "status": "Pending"},
        {"queue_id": 3, "menu": "ก๋วยเตี๋ยวเรือ", "total_price": 40.00, "status": "Pending"},
    ]

    # ทดสอบ display_active_queues
    display_active_queues(active_queues)
    