from datetime import datetime, timedelta
import ctypes
#sifresi
#cehdi
#ban statusu
#acar
main_data_dosyasinin_yolu_2 = 'data.config'
try:
    def cari_vaxti_yaz(file_path):
        cari_vaxt = datetime.now()
        formatted_date = cari_vaxt.strftime('%Y-%m-%d %H:%M:%S')

        try:
            with open(file_path, "r") as dosya:
                setrler = dosya.readlines()

            with open(file_path, 'w') as file:
                setrler[2] = formatted_date
                file.writelines(setrler)
                print("Fayla yazıldı:", formatted_date)
                return True
        except FileNotFoundError:
            print("config.data not found")
            return False
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, 'Xəta', 0x10 | 0x100, 500, 300)
            return False




    def read_data(file_path):
            try:
                with open(file_path, 'r') as file:
                    date_str = file.readlines()[2].strip()
                    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except FileNotFoundError:
                return None

    def check_ban_time(file_path):
            current_time = datetime.now()
            last_date = read_data(file_path)

            if last_date is None:
                return ctypes.windll.user32.MessageBoxW(None, 'Fayl oxuna bilmədi', 'Xəta', 0x10 | 0x100, 500, 300)

            time_difference = current_time - last_date
            if time_difference >= timedelta(minutes=15):
                return True
            else:
                return False
            
    def cehdi_yoxla(path):
        try:
            with open(path,'r') as fayl:
                datalar = fayl.readlines()
                return datalar[1].strip()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, 'Xəta', 0x10 | 0x100, 500, 300)


    def sifre_yoxla(path):
        try:
            with open(path,'r') as fayl:
                sifre = fayl.readlines()[0]
                return sifre.strip()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, 'Xəta', 0x10 | 0x100, 500, 300)



    def sifre_update(path,pw):
        try:
            with open(path,'r') as fayl:
                setrler = fayl.readlines()
            with open(path,'w') as fayl:
                setrler[0] = str(pw) + '\n'
                fayl.writelines(setrler)

        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, 'Xəta', 0x10 | 0x100, 500, 300)


    def cehdi_yenile(path,s):
        try:
            with open(path,'r') as fayl:
                setrler = fayl.readlines()
            with open(path,'w') as fayl:
                setrler[1] = str(s) + '\n'
                fayl.writelines(setrler)

        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, 'Xəta', 0x10 | 0x100, 500, 300)




    def acari_yenile(acar,path=main_data_dosyasinin_yolu_2):
        try:
            with open(path,'r') as fayl:
                setrler = fayl.readlines()
            with open(path,'w') as fayl:
                setrler[3] = str(acar) + '\n'
                fayl.writelines(setrler)

        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, 'Xəta', 0x10 | 0x100, 500, 300)



    def acari_yoxla(path=main_data_dosyasinin_yolu_2):
        try:
            with open(path,'r') as fayl:
                acar = fayl.readlines()[3]
                return str(acar.strip())
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, 'Xəta', 0x10 | 0x100, 500, 300)

except PermissionError as pe:
    ctypes.windll.user32.MessageBoxW(None, pe, 'Bu qovluğa icazə yoxdur', 0x10 | 0x100, 500, 300)

except FileNotFoundError as fnt:
    ctypes.windll.user32.MessageBoxW(None, fnt, 'Fayl tapılmadı', 0x10 | 0x100, 500, 300)
    
    
    
#acari_yenile('C:\Program Files (x86)\Encrypter App\data.config',"key_none")
#print(sifre_yoxla('C:\Program Files (x86)\Encrypter App\data.config'))
#print(cehdi_yoxla('C:\Program Files (x86)\Encrypter App\data.config'))
#cehdi_yenile('C:\Program Files (x86)\Encrypter App\data.config',4)
#print(acari_yoxla('C:\Program Files (x86)\Encrypter App\data.config'))
