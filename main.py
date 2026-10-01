import asyncio
import os
from pyrogram import Client

# أدخل بياناتك من موقع my.telegram.org
API_ID = 22623442  # استبدله بـ api_id الخاص بك
API_HASH = "6584ed44fb15759e98289d8d0324ff71"  # استبدله بـ api_hash الخاص بك

app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

async def change_profile_photo():
    async with app:
        while True:
            photo_path = "photo.jpg"
            
            if os.path.exists(photo_path):
                await app.set_profile_photo(photo=photo_path)
                print("تم تغيير صورة الملف الشخصي بنجاح!")
            else:
                print(f"الصورة {photo_path} غير موجودة!")

            # الانتظار 5 دقائق (300 ثانية)
            await asyncio.sleep(300)

if __name__ == "__main__":
    app.run(change_profile_photo())
  
