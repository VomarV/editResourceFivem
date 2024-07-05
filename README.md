# editResourceFivem

`editResourceFivem` هي أداة Python تهدف إلى تحديث ملفات الموارد في مشاريع **FiveM** من `__resource.lua` إلى `fxmanifest.lua`، وتحديث محتوى الملفات بما يتماشى مع المواصفات الجديدة.

## المتطلبات

- Python 3.6 أو أحدث.

## التثبيت

1. استنسخ هذا المستودع أو حمل الشيفرة البرمجية.

    ```bash
    git clone https://github.com/VomarV/editResourceFivem.git
    ```

2. انتقل إلى دليل المشروع.

    ```bash
    cd editResourceFivem
    ```

## الاستخدام

1. قم بتشغيل الأداة من خلال تنفيذ ملف `editResourceFivem.py`:

    ```bash
    python editResourceFivem.py
    ```

2. أدخل المسار إلى الدليل الذي يحتوي على ملفات الموارد الخاصة بك عندما يُطلب منك ذلك.

3. ستقوم الأداة بالبحث عن الملفات المسماة `__resource.lua` وتغيير اسمها إلى `fxmanifest.lua`. وستتأكد أيضًا من أن الملفات تحتوي على الإعدادات الصحيحة:

    - ستحذف أي سطر يحتوي على `resource_manifest_version`.
    - ستضيف الأسطر التالية إذا لم تكن موجودة بالفعل:
        ```lua
        fx_version 'cerulean'
        games { 'gta5' }
        lua54 'yes'
        ```

## المساهمة

إذا كنت ترغب في المساهمة في هذا المشروع، يمكنك فتح مشاكل جديدة أو تقديم طلبات سحب. نرحب بجميع المساهمات!

