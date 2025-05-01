import os, shutil, time

def simulate_rename_attack():
    os.makedirs("test_dir1/Downloads", exist_ok=True)
    os.makedirs("test_dir1/Startup", exist_ok=True)

    fake_doc = "test_dir1/Downloads/invoice.pdf"
    renamed = "test_dir1/Downloads/invoice.pdf.exe"
    dropped = "test_dir1/Startup/invoice.pdf.exe"

    with open(fake_doc, "w") as f:
        f.write("Totally not malware.")

    time.sleep(1)
    os.rename(fake_doc, renamed)

    time.sleep(1)
    shutil.move(renamed, dropped)

if __name__ == "__main__":
    simulate_rename_attack()
