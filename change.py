import os
import glob

def process_files(directory):
    # البحث عن جميع الملفات __resource.lua في المسار المحدد
    for file_path in glob.glob(os.path.join(directory, '**', '__resource.lua'), recursive=True):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # تحقق مما إذا كان هناك سطر يحتوي على كلمة game أو games
        contains_games = any('games' in line or 'game' in line for line in lines)
        contains_lua = any('lua54' in line for line in lines)
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                # إزالة أي سطر يحتوي على resource_manifest_version
                if 'resource_manifest_version' not in line:
                    file.write(line)
            # إضافة السطر الجديد
            file.write("\nfx_version 'cerulean'\n")
            
            # إضافة سطر games { 'gta5' } إذا لم يكن موجودًا بالفعل
            if not contains_games:
                file.write("games { 'gta5' }\n")


            # إضافة سطر lua54 'yes' إذا لم يكن موجودًا بالفعل
            if not contains_lua:
                file.write("lua54 'yes'\n")

        # تغيير اسم الملف إلى fxmanifest.lua
        new_file_path = file_path.replace('__resource.lua', 'fxmanifest.lua')
        os.rename(file_path, new_file_path)
        print(f"Processed and renamed: {file_path} -> {new_file_path}")

# تحديد المسار الرئيسي الذي ترغب في معالجة الملفات داخله
main_directory = 'D:/Dev/MyFile/NewQB/resources'
process_files(main_directory)