tasks = []


def add_task():
	"""เพิ่มงานใหม่: รับ title, description, due_date แล้วเก็บไว้ใน `tasks` list

	โครงสร้างแต่ละงานเป็น dict ที่มี key: id, title, description, due_date, completed
	"""

	title = input("ชื่อเรื่อง: ").strip()
	description = input("รายละเอียด: ").strip()
	due_date = input("วันครบกำหนด (YYYY-MM-DD หรือข้อความ): ").strip()

	# หาค่า id ถัดไป (1-based)
	next_id = max([t['id'] for t in tasks], default=0) + 1

	task = {
		'id': next_id,
		'title': title,
		'description': description,
		'due_date': due_date,
		'completed': False,
	}

	tasks.append(task)
	print(f"เพิ่มงานเรียบร้อย (id={next_id})")


def view_tasks():
	"""ดูงานทั้งหมด (empty)"""
	pass


def edit_task():
	"""แก้ไขงาน (empty)"""
	pass


def delete_task():
	"""ลบงาน (empty)"""
	pass


def exit_program():
	"""ออกจากโปรแกรม (empty)"""
	pass


def main_menu():
	while True:
		print("\nเมนูหลัก:")
		print("1. เพิ่มงานใหม่")
		print("2. ดูงานทั้งหมด")
		print("3. แก้ไขงาน")
		print("4. ลบงาน")
		print("5. ออกจากโปรแกรม")
		choice = input("เลือกหมายเลข: ").strip()

		if choice == "1":
			add_task()
		elif choice == "2":
			view_tasks()
		elif choice == "3":
			edit_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			exit_program()
			break
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง.")


if __name__ == "__main__":
	main_menu()

 