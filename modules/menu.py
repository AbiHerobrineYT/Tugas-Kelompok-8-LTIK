def menu_utama():
    while True:
        print("================ RUANG TEDUH =============")

        print("Halo! Apa yang ingin kamu lakukan hari ini?\n")

        print("[1] 📝 Mulai Tes Kesehatan Mental")
        print("[2] 📊 Lihat Riwayat Hasil Saya")
        print("[3] ✅ To-Do List & Self Care")
        print("[4] ℹ️ Tentang Aplikasi (Disclaimer)")
        print("[5] 🚪 Keluar Aplikasi")

        print("\n" + "-"*40)

        pilihan = ['1', '2', '3', '4', '5']
        user_input = input("Pilih menu (1-5) : ")
        if user_input in pilihan:
            return user_input
        else:
            print("Pilihan tidak valid. Mohon pilih 1-5...")

#tes
